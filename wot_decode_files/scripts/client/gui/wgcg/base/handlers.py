# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/base/handlers.py
from gui.wgcg.settings import WebRequestDataType

class RequestHandlers(object):

    def __init__(self, requester):
        self._requester = requester


class BaseRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.LOGIN: self.__login, 
           WebRequestDataType.LOGOUT: self.__logout, 
           WebRequestDataType.PING: self.__ping}
        return handlers

    def __login(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, 'login', ctx.getUserDatabaseID(), ctx.getTokenID(), ctx.isJwt())

    def __logout(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, 'logout')

    def __ping(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, 'get_alive_status')