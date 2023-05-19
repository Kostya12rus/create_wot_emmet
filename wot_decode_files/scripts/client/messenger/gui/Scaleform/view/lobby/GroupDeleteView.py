# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/GroupDeleteView.py
from gui.Scaleform.locale.MESSENGER import MESSENGER
from messenger.gui.Scaleform.meta.GroupDeleteViewMeta import GroupDeleteViewMeta
from messenger import normalizeGroupId
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter

class GroupDeleteView(GroupDeleteViewMeta):

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return

    def onOk(self, data):
        self.proto.contacts.removeGroup(normalizeGroupId(data.groupName), data.deleteWithMembers)
        self.as_closeViewS()

    def _getInitDataObject(self):
        initData = self._getDefaultInitData(MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_DELETEGROUP_MAINLABEL, MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_DELETEGROUP_BTNOK_LABEL, MESSENGER.MESSENGER_CONTACTS_VIEW_MANAGEGROUP_DELETEGROUP_BTNCANCEL_LABEL, MESSENGER.CONTACTS_GROUPDELETEVIEW_TOOLTIPS_BTNS_APPLY, MESSENGER.CONTACTS_GROUPDELETEVIEW_TOOLTIPS_BTNS_CLOSE)
        return initData