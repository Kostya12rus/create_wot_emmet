# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/dummy/df_controller.py
import Event
from festivity.base import FestivityQuestsHangarFlag
from skeletons.gui.game_control import IFestivityController
_DEFAULT_QUESTS_FLAG = FestivityQuestsHangarFlag(None, None, None)

class DummyController(IFestivityController):

    def __init__(self):
        super(DummyController, self).__init__()
        self.__state = None
        self.__em = Event.EventManager()
        self.onStateChanged = Event.Event(self.__em)
        return

    def isEnabled(self):
        return False

    def getHangarQuestsFlagData(self):
        return _DEFAULT_QUESTS_FLAG