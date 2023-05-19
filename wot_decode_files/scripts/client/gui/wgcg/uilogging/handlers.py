# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/uilogging/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class UILoggingRequestHandlers(RequestHandlers):

    def get(self):
        return {WebRequestDataType.UI_LOGGING_SESSION: self.__getSession}

    def __getSession(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('uilogging', 'get_uilogging_session'))