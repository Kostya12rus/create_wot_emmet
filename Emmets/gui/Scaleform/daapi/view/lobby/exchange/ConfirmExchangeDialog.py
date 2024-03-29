# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/exchange/ConfirmExchangeDialog.py
from adisp import adisp_process
from gui import SystemMessages
from gui.Scaleform.daapi.view.meta.ConfirmExchangeDialogMeta import ConfirmExchangeDialogMeta

class ConfirmExchangeDialog(ConfirmExchangeDialogMeta):

    def __init__(self, meta, handler):
        super(ConfirmExchangeDialog, self).__init__()
        self.handler = handler
        self.__exchangeMutex = False
        self.__setMeta(meta)

    def updateDialog(self, meta, handler):
        if self.handler is not None:
            self._callHandler(False)
        self.handler = handler
        self.__removeMeta()
        self.__exchangeMutex = False
        self.__setMeta(meta)
        self.__prepareAndSendData()
        return

    def onWindowClose(self):
        self._callHandler(False)
        self.destroy()

    @adisp_process
    def exchange(self, goldValue):
        if self.__exchangeMutex:
            return
        else:
            self.__exchangeMutex = True
            exchangedValue = goldValue * self.meta.getExchangeRate()
            result = yield self.meta.submit(goldValue, exchangedValue)
            if result is not None:
                SystemMessages.pushMessagesFromResult(result)
            if result is not None and result.success and self.meta is not None:
                self._callHandler(True, self.meta.getTypeCompDescr())
                self.destroy()
            else:
                self.__exchangeMutex = False
            return

    def _populate(self):
        super(ConfirmExchangeDialog, self)._populate()
        self.__prepareAndSendData()

    def _dispose(self):
        self.__removeMeta()
        self.handler = None
        super(ConfirmExchangeDialog, self)._dispose()
        return

    def _callHandler(self, success, *kwargs):
        if self.handler is not None:
            self.handler((success, kwargs))
        return

    def __removeMeta(self):
        if self.meta is not None:
            self.meta.onInvalidate -= self.__prepareAndSendData
            self.meta.onCloseDialog -= self.onWindowClose
            self.meta.destroy()
            self.meta = None
        return

    def __setMeta(self, meta):
        self.meta = meta
        self.meta.onInvalidate += self.__prepareAndSendData
        self.meta.onCloseDialog += self.onWindowClose

    def __prepareAndSendData(self, *args):
        self.as_updateS(self.meta.makeVO())