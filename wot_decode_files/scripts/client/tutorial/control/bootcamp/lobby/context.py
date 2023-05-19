# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/bootcamp/lobby/context.py
from tutorial.control import context
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class BootcampLobbyStartReqs(context.StartReqs):

    def isEnabled(self):
        return self.bootcampController.isInBootcamp()

    def prepare(self, ctx):
        pass

    def process(self, descriptor, ctx):
        return True


class BootcampBonusesRequester(context.BonusesRequester):
    bootcampController = dependency.descriptor(IBootcampController)

    def __init__(self):
        lessonNum = self.bootcampController.getLessonNum()
        wonBattlesMask = (1 << lessonNum) - 1
        super(BootcampBonusesRequester, self).__init__(completed=wonBattlesMask)

    def setCompleted(self, _):
        pass

    def request(self, _=None):
        pass