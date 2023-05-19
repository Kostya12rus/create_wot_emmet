# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/exchange/BaseExchangeWindow.py
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.BaseExchangeWindowMeta import BaseExchangeWindowMeta

class BaseExchangeWindow(BaseExchangeWindowMeta):

    def __init__(self, ctx=None):
        super(BaseExchangeWindow, self).__init__(self)

    def _populate(self):
        super(BaseExchangeWindow, self)._populate()
        self._subscribe()

    def _subscribe(self):
        pass

    def _setGoldCallBack(self, gold):
        self.as_setPrimaryCurrencyS(gold)

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(BaseExchangeWindow, self)._dispose()