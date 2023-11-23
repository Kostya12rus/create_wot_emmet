# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/event_boards/settings.py


class _EventBoardSettings(object):

    def __init__(self):
        self.__minimized = {}

    def isGroupMinimized(self, event):
        groupID = event.getEventID()
        if groupID in self.__minimized:
            return self.__minimized[groupID]
        return event.isFinished()

    def updateExpanded(self, event, value):
        groupID = event.getEventID()
        self.__minimized[groupID] = not value


_settings = _EventBoardSettings()

def isGroupMinimized(event):
    return _settings.isGroupMinimized(event)


def expandGroup(event, isExpanded):
    _settings.updateExpanded(event, isExpanded)