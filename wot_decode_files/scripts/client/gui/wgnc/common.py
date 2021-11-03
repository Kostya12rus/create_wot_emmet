# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/common.py
from debug_utils import LOG_WARNING

class WebHandlersContainer(object):
    _webHandlers = {}

    @classmethod
    def addWebHandler(cls, name, handler):
        cls._webHandlers[name] = handler

    @classmethod
    def removeWebHandler(cls, name):
        if name in cls._webHandlers:
            del cls._webHandlers[name]

    @classmethod
    def getWebHandler(cls, name):
        if name:
            handler = cls._webHandlers.get(name)
        else:
            handler = None
        if not handler:
            LOG_WARNING("Wrong web-client handler's name '%s'" % name)
        return handler