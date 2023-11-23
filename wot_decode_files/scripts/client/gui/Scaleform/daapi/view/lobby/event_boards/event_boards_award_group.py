# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_award_group.py
from gui.Scaleform.daapi.view.meta.AwardGroupsMeta import AwardGroupsMeta
import Event

class EventBoardsAwardGroup(AwardGroupsMeta):

    def __init__(self):
        super(EventBoardsAwardGroup, self).__init__()
        self.onShowRewardCategory = Event.Event()

    def showGroup(self, groupId):
        self.onShowRewardCategory(groupId)

    def setActiveRewardGroup(self, groupID):
        self.as_setSelectedS(groupID - 1, True)