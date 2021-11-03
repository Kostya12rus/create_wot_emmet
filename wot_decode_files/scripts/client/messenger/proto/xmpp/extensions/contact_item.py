# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/contact_item.py
from messenger.proto.xmpp.extensions import PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.wg_items import WgSharedExtension
from messenger.proto.xmpp.jid import ContactJID

class ContactItemExtension(PyExtension):

    def __init__(self, jid=None):
        super(ContactItemExtension, self).__init__(_TAG.ITEM)
        if jid:
            self.setAttribute('jid', str(jid))
        self.setChild(WgSharedExtension())

    @classmethod
    def getDefaultData(cls):
        return (None, WgSharedExtension.getDefaultData())

    def parseTag(self, pyGlooxTag):
        jid = pyGlooxTag.findAttribute('jid')
        if jid:
            jid = ContactJID(jid)
        else:
            jid = None
        info = self._getChildData(pyGlooxTag, 0, WgSharedExtension.getDefaultData())
        return (
         jid, info)