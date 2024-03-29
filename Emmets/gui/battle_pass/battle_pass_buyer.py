# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/battle_pass_buyer.py
import logging
from gui import SystemMessages
from adisp import adisp_async, adisp_process
from gui.battle_pass.battle_pass_constants import ChapterState
from gui.shared.gui_items.processors.battle_pass import BuyBattlePass, BuyBattlePassLevels
from gui.shared.utils import decorators
from gui.shared.money import Currency
from gui.shop import showBuyGoldForBattlePass, showBuyGoldForBattlePassLevels
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController, ISoundEventChecker
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class BattlePassBuyer(object):
    __itemsCache = dependency.descriptor(IItemsCache)
    __battlePassController = dependency.descriptor(IBattlePassController)
    __soundEventChecker = dependency.descriptor(ISoundEventChecker)

    @classmethod
    @decorators.adisp_process('buyBattlePass')
    def buyBP(cls, seasonID, chapterID, onBuyCallback=None):
        spendMoneyGold = 0
        if chapterID not in cls.__battlePassController.getChapterIDs():
            _logger.error('Invalid chapterID: %s!', chapterID)
            return
        if not cls.__battlePassController.isBought(chapterID=chapterID):
            spendMoneyGold += cls.__battlePassController.getBattlePassCost(chapterID).get(Currency.GOLD, 0)
        result = False
        if cls.__itemsCache.items.stats.actualGold < spendMoneyGold:
            showBuyGoldForBattlePass(spendMoneyGold)
        else:
            result = yield cls.__buyBattlePass(seasonID, chapterID)
        if onBuyCallback:
            onBuyCallback(result)

    @classmethod
    @decorators.adisp_process('buyBattlePassLevels')
    def buyLevels(cls, seasonID, chapterID, levels=0, onBuyCallback=None):
        if chapterID not in cls.__battlePassController.getChapterIDs():
            _logger.error('Invalid chapterID: %s!', chapterID)
            return
        if cls.__battlePassController.getChapterState(chapterID) != ChapterState.ACTIVE:
            _logger.error('Chapter %s should be active to buy levels at it!', chapterID)
            return
        spendMoneyGold = 0
        if levels > 0:
            spendMoneyGold += cls.__itemsCache.items.shop.getBattlePassLevelCost().get(Currency.GOLD, 0) * levels
        result = False
        if cls.__itemsCache.items.stats.actualGold < spendMoneyGold:
            showBuyGoldForBattlePassLevels(spendMoneyGold)
        else:
            cls.__soundEventChecker.lockPlayingSounds()
            result = yield cls.__buyBattlePassLevels(seasonID, chapterID, levels)
            cls.__soundEventChecker.unlockPlayingSounds()
        if onBuyCallback:
            onBuyCallback(result)

    @classmethod
    @adisp_async
    @adisp_process
    def __buyBattlePass(cls, seasonID, chapterID, callback):
        result = yield BuyBattlePass(seasonID, chapterID).request()
        startLevel, _ = cls.__battlePassController.getChapterLevelInterval(chapterID)
        if cls.__battlePassController.getLevelInChapter(chapterID) != startLevel - 1:
            callback(result.success)
            return
        else:
            if result.userMsg is not None:
                SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType, messageData=result.auxData)
            callback(result.success)
            return

    @staticmethod
    @adisp_async
    @adisp_process
    def __buyBattlePassLevels(seasonID, chapterID, levels, callback):
        result = yield BuyBattlePassLevels(seasonID, chapterID, levels).request()
        if result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        callback(result.success)