# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactsSettingsViewMeta.py
from messenger.gui.Scaleform.view.lobby.BaseContactView import BaseContactView

class ContactsSettingsViewMeta(BaseContactView):

    def showOfflineUsers(self, value):
        self._printOverrideError('showOfflineUsers')

    def showOthers(self, value):
        self._printOverrideError('showOthers')

    def messagesNotFromContacts(self, value):
        self._printOverrideError('messagesNotFromContacts')