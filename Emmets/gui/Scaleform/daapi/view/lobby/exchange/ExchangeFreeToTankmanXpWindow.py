# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/exchange/ExchangeFreeToTankmanXpWindow.py
from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl.lobby.crew.confirm_skills_learn_dialog import ConfirmSkillsLearnDialogData
from gui.Scaleform.daapi.view.meta.ExchangeFreeToTankmanXpWindowMeta import ExchangeFreeToTankmanXpWindowMeta
from gui.shared.events import SkillDropEvent
from gui.shared.gui_items.processors.tankman import TankmanFreeToOwnXpConvertor
from gui.shared.gui_items.serializers import packTankmanSkill
from gui.shared.money import Money
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.utils import decorators
from helpers import dependency
from items.tankmen import MAX_SKILL_LEVEL
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache
from wg_async import wg_await, wg_async

class ExchangeFreeToTankmanXpWindow(ExchangeFreeToTankmanXpWindowMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    wallet = dependency.descriptor(IWalletController)

    def __init__(self, ctx=None):
        super(ExchangeFreeToTankmanXpWindow, self).__init__()
        self.__tankManId = ctx.get('tankManId')
        self.__selectedXpForConvert = 0
        self.__selectedLevel = 0

    def apply(self):
        self.doRequest()

    @wg_async
    def doRequest(self):
        tankman = self.itemsCache.items.getTankman(self.__tankManId)
        from gui.shared.event_dispatcher import showLearnConfirmDialog
        result = yield wg_await(showLearnConfirmDialog(ConfirmSkillsLearnDialogData(tmanInvID=self.__tankManId, skill=tankman.skills[-1], xpAmount=self.__selectedXpForConvert, level=self.__selectedLevel)))
        if not result.busy:
            isOk, _ = result.result
            if isOk:
                self.__processTankmanFreeToOwnXpConvertor(tankman)

    @decorators.adisp_process('updatingSkillWindow')
    def __processTankmanFreeToOwnXpConvertor(self, tankman):
        xpConverter = TankmanFreeToOwnXpConvertor(tankman, self.__selectedXpForConvert)
        result = yield xpConverter.request()
        if result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
        if result.success:
            self.onWindowClose()

    def calcValueRequest(self, toLevel):
        items = self.itemsCache.items
        tankman = items.getTankman(self.__tankManId)
        tankmanDescriptor = tankman.descriptor
        if toLevel == tankmanDescriptor.lastSkillLevel:
            self.__selectedXpForConvert = 0
            self.as_setCalcValueResponseS(0, None)
            return
        else:
            toLevel = int(toLevel)
            if toLevel > MAX_SKILL_LEVEL:
                toLevel = MAX_SKILL_LEVEL
            needXp = self.__getCurrentTankmanLevelCost(tankman)
            for level in range(int(tankmanDescriptor.lastSkillLevel + 1), toLevel, 1):
                needXp += self.__calcLevelUpCost(tankman, level, tankmanDescriptor.lastSkillNumber - tankmanDescriptor.freeSkillsNumber)

            rate = items.shop.freeXPToTManXPRate
            roundedNeedXp = self.__roundByModulo(needXp, rate)
            xpWithDiscount = roundedNeedXp / rate
            self.__selectedXpForConvert = max(1, xpWithDiscount)
            self.__selectedLevel = toLevel
            defaultRate = items.shop.defaults.freeXPToTManXPRate
            if defaultRate and defaultRate != 0:
                defaultRoundedNeedXp = self.__roundByModulo(needXp, defaultRate)
                defaultXpWithDiscount = defaultRoundedNeedXp / defaultRate
                defaultXpForConvert = max(1, defaultXpWithDiscount)
            else:
                defaultXpForConvert = self.__selectedXpForConvert
            actionPriceData = None
            if self.__selectedXpForConvert != defaultXpForConvert:
                actionPriceData = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, 'freeXPToTManXPRate', True, Money(gold=self.__selectedXpForConvert), Money(gold=defaultXpForConvert))
            self.as_setCalcValueResponseS(self.__selectedXpForConvert, actionPriceData)
            return

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(ExchangeFreeToTankmanXpWindow, self)._populate()
        self.as_setWalletStatusS(self.wallet.status)
        g_clientUpdateManager.addCallbacks({'stats.freeXP': self.__onFreeXpChanged, 
           'inventory.8.compDescr': self.__onTankmanChanged})
        self.addListener(SkillDropEvent.SKILL_DROPPED_SUCCESSFULLY, self.__skillDropWindowCloseHandler)
        self.wallet.onWalletStatusChanged += self.__setWalletCallback
        self.itemsCache.onSyncCompleted += self.__onFreeXpChanged
        self.__prepareAndSendInitData()

    def _dispose(self):
        self.removeListener(SkillDropEvent.SKILL_DROPPED_SUCCESSFULLY, self.__skillDropWindowCloseHandler)
        self.itemsCache.onSyncCompleted -= self.__onFreeXpChanged
        self.wallet.onWalletStatusChanged -= self.__setWalletCallback
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(ExchangeFreeToTankmanXpWindow, self)._dispose()

    def __onFreeXpChanged(self, *args):
        self.__prepareAndSendInitData()

    def __onTankmanChanged(self, data):
        if self.__tankManId in data:
            if data[self.__tankManId] is None:
                self.destroy()
                return
            self.__prepareAndSendInitData()
        return

    def __prepareAndSendInitData(self):
        items = self.itemsCache.items
        tankman = items.getTankman(self.__tankManId)
        if tankman is None or not tankman.skills:
            return
        rate = items.shop.freeXPToTManXPRate
        toNextPrcLeft = self.__getCurrentTankmanLevelCost(tankman)
        tDescr = tankman.descriptor
        nextSkillLevel = tDescr.lastSkillLevel
        freeXp = items.stats.freeXP
        if freeXp >= self.__roundByModulo(toNextPrcLeft, rate) / rate:
            nextSkillLevel += 1
            skillNumber = tDescr.lastSkillNumber - tDescr.freeSkillsNumber
            while nextSkillLevel < MAX_SKILL_LEVEL:
                toNextPrcLeft += self.__calcLevelUpCost(tankman, nextSkillLevel, skillNumber)
                if freeXp < self.__roundByModulo(toNextPrcLeft, rate) / rate:
                    break
                nextSkillLevel += 1

        data = {'tankmanID': self.__tankManId, 'currentSkill': packTankmanSkill(tankman.skills[len(tankman.skills) - 1]), 
           'lastSkillLevel': tDescr.lastSkillLevel, 
           'nextSkillLevel': nextSkillLevel}
        self.as_setInitDataS(data)
        return

    def __getCurrentTankmanLevelCost(self, tankman):
        if tankman.roleLevel != MAX_SKILL_LEVEL or tankman.skills and tankman.descriptor.lastSkillLevel != MAX_SKILL_LEVEL:
            tankmanDescriptor = tankman.descriptor
            lastSkillNumberValue = tankmanDescriptor.lastSkillNumber - tankmanDescriptor.freeSkillsNumber
            if lastSkillNumberValue == 0 or tankman.roleLevel != MAX_SKILL_LEVEL:
                nextSkillLevel = tankman.roleLevel
            else:
                nextSkillLevel = tankmanDescriptor.lastSkillLevel
            skillSeqNum = 0
            if tankman.roleLevel == MAX_SKILL_LEVEL:
                skillSeqNum = lastSkillNumberValue
            return self.__calcLevelUpCost(tankman, nextSkillLevel, skillSeqNum) - tankmanDescriptor.freeXP
        return 0

    def __calcLevelUpCost(self, tankman, fromLevel, skillSeqNum):
        return tankman.descriptor.levelUpXpCost(fromLevel, skillSeqNum)

    def __roundByModulo(self, targetXp, rate):
        left_rate = targetXp % rate
        if left_rate > 0:
            targetXp += rate - left_rate
        return targetXp

    def __skillDropWindowCloseHandler(self, event):
        self.destroy()

    def __setWalletCallback(self, status):
        self.__prepareAndSendInitData()
        self.as_setWalletStatusS(status)