# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/craftmachine/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class CraftmachineRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.CRAFTMACHINE_MODULES_INFO: self.__modulesInfo}
        return handlers

    def __modulesInfo(self, ctx, callback):
        reqCtx = self._requester.doRequestEx(ctx, callback, ('craftmachine', 'craftmachine_modules_info'))
        return reqCtx