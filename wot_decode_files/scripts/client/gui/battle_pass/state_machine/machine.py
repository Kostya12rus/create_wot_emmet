# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/state_machine/machine.py
import logging, typing
from frameworks.state_machine import ConditionTransition, StateMachine
from gui.battle_pass.state_machine import lockNotificationManager, states
from gui.battle_pass.state_machine.state_machine_helpers import isProgressionComplete, packToken
if typing.TYPE_CHECKING:
    from typing import Dict, Iterable, List, Optional
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

class BattlePassStateMachine(StateMachine):
    __slots__ = ('__rewards', '__data', '__rewardsToChoose', '__packageRewards', '__chapterStyle',
                 '__manualFlow')

    def __init__(self):
        super(BattlePassStateMachine, self).__init__()
        self.__rewards = None
        self.__data = None
        self.__rewardsToChoose = []
        self.__packageRewards = None
        self.__chapterStyle = None
        self.__manualFlow = False
        return

    def stop(self):
        self.clearSelf()
        lockNotificationManager(False)
        super(BattlePassStateMachine, self).stop()

    def post(self, event):
        if self.isRunning():
            super(BattlePassStateMachine, self).post(event)

    @property
    def lobby(self):
        return self.getChildByIndex(0)

    @property
    def video(self):
        return self.getChildByIndex(1)

    @property
    def choice(self):
        return self.getChildByIndex(2)

    @property
    def reward(self):
        return self.getChildByIndex(3)

    def configure(self):
        lobbyState = states.LobbyState()
        choiceState = states.ChoiceState()
        rewardState = states.RewardState()
        videoState = states.VideoState()
        lobbyState.configure()
        choiceState.configure()
        rewardState.configure()
        lobbyState.lobbyWait.addTransition(ConditionTransition(self.__hasChoiceOption, priority=2), target=choiceState.choiceItem)
        lobbyState.lobbyWait.addTransition(ConditionTransition(self.__hasStyleReward, priority=1), target=videoState)
        lobbyState.lobbyWait.addTransition(ConditionTransition(self.__hasAnyReward, priority=0), target=rewardState.rewardAny)
        choiceState.choiceItem.addTransition(ConditionTransition(self.__hasStyleReward, priority=2), target=videoState)
        choiceState.choiceItem.addTransition(ConditionTransition(self.__hasAnyReward, priority=1), target=rewardState.rewardAny)
        choiceState.choiceItem.addTransition(ConditionTransition((lambda _: True), priority=0), target=lobbyState.lobbyWait)
        videoState.addTransition(ConditionTransition((lambda _: True), priority=0), target=rewardState.rewardStyle)
        rewardState.rewardAny.addTransition(ConditionTransition(isProgressionComplete, priority=1), target=lobbyState.lobbyFinal)
        rewardState.rewardAny.addTransition(ConditionTransition((lambda _: True), priority=0), target=lobbyState.lobbyWait)
        self.addState(lobbyState)
        self.addState(videoState)
        self.addState(choiceState)
        self.addState(rewardState)

    def hasActiveFlow(self):
        return not self.isStateEntered(states.BattlePassRewardStateID.LOBBY)

    def saveRewards(self, rewardsToChoose, defaultRewards, chapterStyle, data, packageRewards):
        self.__rewardsToChoose = rewardsToChoose
        self.__rewards = defaultRewards
        self.__packageRewards = packageRewards
        self.__chapterStyle = chapterStyle
        self.__data = data

    def setManualFlow(self):
        self.__manualFlow = True

    def getRewardsData(self):
        return (
         self.__rewards, self.__data, self.__packageRewards)

    def extendRewards(self, rewards):
        if not self.__rewards:
            self.__rewards = []
        self.__rewards.extend(rewards)

    def getRewardsToChoose(self):
        return tuple(self.__rewardsToChoose)

    def hasRewardToChoose(self):
        return bool(self.__rewardsToChoose)

    def removeRewardToChoose(self, tokenID, isTaken):
        if isTaken:
            if tokenID in self.__rewardsToChoose:
                self.__rewardsToChoose.remove(tokenID)
        else:
            if self.__rewards is None:
                self.__rewards = []
            if not self.__manualFlow:
                self.__rewards.append(packToken(tokenID))
            self.__rewardsToChoose.remove(tokenID)
        return

    def getChosenStyleChapter(self):
        return self.__chapterStyle

    def setChapterForStyle(self, chapter):
        self.__chapterStyle = chapter

    def getLeftRewardsCount(self):
        return len(self.__rewardsToChoose)

    def clearChapterStyle(self):
        self.__chapterStyle = None
        return

    def clearManualFlow(self):
        self.__manualFlow = False

    def clearSelf(self):
        self.__rewards = None
        self.__packageRewards = None
        self.__data = None
        self.__rewardsToChoose = []
        self.__chapterStyle = None
        self.__manualFlow = False
        return

    def __hasStyleReward(self, *_):
        return self.__chapterStyle is not None

    def __hasChoiceOption(self, *_):
        return bool(self.__rewardsToChoose)

    def __hasAnyReward(self, *_):
        return bool(self.__rewards) or bool(self.__packageRewards)