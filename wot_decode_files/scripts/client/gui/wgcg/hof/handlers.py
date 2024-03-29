# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/hof/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class HofRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.HOF_USER_INFO: self.__hofUserInfo, 
           WebRequestDataType.HOF_USER_EXCLUDE: self.__hofUserExclude, 
           WebRequestDataType.HOF_USER_RESTORE: self.__hofUserRestore}
        return handlers

    def __hofUserInfo(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('wgrms', 'hof_user_info'))

    def __hofUserExclude(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('wgrms', 'hof_user_exclude'))

    def __hofUserRestore(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('wgrms', 'hof_user_restore'))