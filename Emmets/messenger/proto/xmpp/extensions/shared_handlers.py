# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/shared_handlers.py
from messenger.proto.xmpp.extensions import PyHandler

class IQHandler(PyHandler):

    def getFilterString(self):
        return ('/iq/{0}').format(self._ext.getXPath())


class IQChildHandler(PyHandler):
    __slots__ = ('_index', )

    def __init__(self, ext, index=0):
        super(IQChildHandler, self).__init__(ext)
        self._index = index

    def getFilterString(self):
        return ('/iq/{0}').format(self._ext.getXPath(self._index))

    def handleTag(self, pyGlooxTag):
        child = self._ext.getChild(self._index)
        if not child:
            return
        result = pyGlooxTag.filterXPath(self.getFilterString())
        for tag in result:
            data = child.parseTag(tag)
            if data:
                yield data


class ProxyHandler(PyHandler):

    def getFilterString(self):
        return self._ext.getXPath()