# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ContactsTreeComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContactsTreeComponentMeta(BaseDAAPIComponent):

    def onGroupSelected(self, mainGroup, groupData):
        self._printOverrideError('onGroupSelected')

    def searchLocalContact(self, flt):
        self._printOverrideError('searchLocalContact')

    def hasDisplayingContacts(self):
        self._printOverrideError('hasDisplayingContacts')

    def as_updateInfoMessageS(self, enableSearchInput, title, message, warn):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInfoMessage(enableSearchInput, title, message, warn)

    def as_getMainDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMainDP()

    def as_setInitDataS(self, val):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(val)