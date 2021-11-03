# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/yha/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class YhaRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.YHA_VIDEO: self.__getYhaVideo}
        return handlers

    def __getYhaVideo(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('yha', 'get_yha_video'))