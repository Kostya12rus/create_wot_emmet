# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/state_machine/delegator.py
import typing
from battle_pass_common import BattlePassRewardReason as BPReason
from frameworks.state_machine import StringEvent, StateEvent
from gui.battle_pass.state_machine.state_machine_helpers import separateRewards
from gui.battle_pass.state_machine.states import StateMachineEventID
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Dict, Iterable, Optional
    from gui.battle_pass.state_machine.machine import BattlePassStateMachine

class BattlePassRewardLogic(object):
    __slots__ = ('__machine', '__startAfterTurningOnMachine')
    __battlePassController = dependency.descriptor(IBattlePassController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, machine):
        super(BattlePassRewardLogic, self).__init__()
        self.__machine = machine
        self.__startAfterTurningOnMachine = False

    def start(self):
        if self.__machine.isRunning():
            return
        self.__machine.configure()
        self.__machine.start()
        if self.__startAfterTurningOnMachine:
            self.postStateEvent()
            self.__startAfterTurningOnMachine = False

    def stop(self):
        self.__machine.stop()
        self.__startAfterTurningOnMachine = False

    def startRewardFlow(self, rewards, data, packageRewards):
        rewardsToChoose, defaultRewards, chapterStyle = separateRewards(rewards, battlePass=self.__battlePassController)
        rewardsToChoose = self.__getValidRewardsToChoose(rewardsToChoose)
        self.__machine.saveRewards(rewardsToChoose, defaultRewards, chapterStyle, data, packageRewards)
        if not self.__machine.isRunning():
            self.__startAfterTurningOnMachine = True
        else:
            self.postStateEvent()

    def startManualFlow(self, rewardsToChoose, chapterID=None, level=0):
        data = {'chapter': self.__getChapterFromRewardsToChoose(rewardsToChoose) if chapterID is None else chapterID, 
           'level': level, 
           'reason': BPReason.SELECT_REWARD}
        self.__machine.saveRewards(rewardsToChoose, None, None, data, None)
        self.__machine.setManualFlow()
        if not self.__machine.isRunning():
            self.__startAfterTurningOnMachine = True
        else:
            self.postStateEvent()
        return

    def hasActiveFlow(self):
        return self.__machine.hasActiveFlow()

    def hasRewardToChoose(self):
        return self.__machine.hasRewardToChoose()

    def getLeftRewardsCount(self):
        return self.__machine.getLeftRewardsCount()

    def getRewardsToChoose(self):
        return self.__machine.getRewardsToChoose()

    def extendRewards(self, rewards):
        self.__machine.extendRewards(rewards)

    def getChosenStyleChapter(self):
        self.__machine.getChosenStyleChapter()

    def setChapterForStyle(self, chapter):
        self.__machine.setChapterForStyle(chapter)

    def postPreviewOpen(self):
        self.postStringEvent(StateMachineEventID.OPEN_PREVIEW)

    def postClosePreview(self):
        self.postStringEvent(StateMachineEventID.CLOSE_PREVIEW)

    def postStringEvent(self, eventID, **kwargs):
        if self.__machine.isRunning():
            self.__machine.post(StringEvent(eventID, **kwargs))

    def postStateEvent(self, **kwargs):
        if self.__machine.isRunning():
            self.__machine.post(StateEvent(**kwargs))

    def __getValidRewardsToChoose(self, rewardsToChoose):
        return [ token for token in rewardsToChoose if bool(self.__itemsCache.items.tokens.getToken(token)) ]

    @staticmethod
    def __getChapterFromRewardsToChoose(rewardsToChoose):
        chapters = set(int(reward.split(':')[-2]) for reward in rewardsToChoose)
        if len(chapters) == 1:
            return next(iter(chapters))
        return 0