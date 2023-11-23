# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/ContactsCMListener.py
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity

class ContactsCMListener(EventSystemEntity):

    def startListenContextMenu(self):
        self.addListener(events.ContactsEvent.EDIT_GROUP, self._onEditGroup, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.ContactsEvent.REMOVE_GROUP, self._onRemoveGroup, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.ContactsEvent.CREATE_CONTACT_NOTE, self._onCreateContactNote, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.ContactsEvent.EDIT_CONTACT_NOTE, self._onEditContactNote, scope=EVENT_BUS_SCOPE.LOBBY)

    def stopListenContextMenu(self):
        self.removeListener(events.ContactsEvent.EDIT_GROUP, self._onEditGroup, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.ContactsEvent.REMOVE_GROUP, self._onRemoveGroup, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.ContactsEvent.CREATE_CONTACT_NOTE, self._onCreateContactNote, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.ContactsEvent.EDIT_CONTACT_NOTE, self._onEditContactNote, scope=EVENT_BUS_SCOPE.LOBBY)

    def _onEditGroup(self, event):
        pass

    def _onRemoveGroup(self, event):
        pass

    def _onCreateContactNote(self, event):
        pass

    def _onEditContactNote(self, event):
        pass