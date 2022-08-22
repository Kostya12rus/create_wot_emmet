# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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