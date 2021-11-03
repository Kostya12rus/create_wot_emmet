# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/control/bootcamp/lobby/context.py
from tutorial.control import context
from helpers import dependency
from skeletons.gui.game_control import IBootcampController

class BootcampLobbyStartReqs(context.StartReqs):

    def prepare(self, ctx):
        pass

    def process(self, descriptor, ctx):
        return True

    def _isBootcamp(self):
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