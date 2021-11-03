# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactsListPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class ContactsListPopoverMeta(SmartPopOverView):

    def addToFriends(self, uid, name):
        self._printOverrideError('addToFriends')

    def addToIgnored(self, uid, name):
        self._printOverrideError('addToIgnored')

    def isEnabledInRoaming(self, uid):
        self._printOverrideError('isEnabledInRoaming')

    def changeGroup(self, dbId, contactName, groupData):
        self._printOverrideError('changeGroup')

    def copyIntoGroup(self, contactDbId, groupData):
        self._printOverrideError('copyIntoGroup')

    def as_setInitInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitInfo(data)

    def as_editGroupS(self, targetGroupName):
        if self._isDAAPIInited():
            return self.flashObject.as_editGroup(targetGroupName)

    def as_removeGroupS(self, targetGroupName):
        if self._isDAAPIInited():
            return self.flashObject.as_removeGroup(targetGroupName)

    def as_createContactNoteS(self, userName, databaseID):
        if self._isDAAPIInited():
            return self.flashObject.as_createContactNote(userName, databaseID)

    def as_editContactNoteS(self, userName, databaseID):
        if self._isDAAPIInited():
            return self.flashObject.as_editContactNote(userName, databaseID)