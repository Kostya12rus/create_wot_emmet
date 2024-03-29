# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/SimpleDialog.py
import BigWorld
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.SimpleDialogMeta import SimpleDialogMeta
from gui.Scaleform.framework import ScopeTemplates

class SimpleDialog(SimpleDialogMeta):

    def __init__(self, message, title, buttons, handler, dialogScope=ScopeTemplates.DEFAULT_SCOPE, timer=0):
        super(SimpleDialog, self).__init__()
        self.__message = message
        self.__title = title
        self.__buttons = buttons
        self.__timer = timer
        self.__timerCallbackID = None
        self._handler = handler
        self.__dialogScope = dialogScope
        self._isProcessed = False
        return

    def _callHandler(self, buttonID):
        if self._handler is not None:
            self._handler(buttonID == DIALOG_BUTTON_ID.SUBMIT)
            self._isProcessed = True
        return

    def getCurrentScope(self):
        if self.__dialogScope is not None:
            self.setCurrentScope(self.__dialogScope)
            self.__dialogScope = None
        return super(SimpleDialog, self).getCurrentScope()

    def _populate(self):
        super(SimpleDialog, self)._populate()
        self.__setMessage()
        self.as_setTitleS(self.__title)
        self.as_setButtonsS(self.__buttons)
        self.setCurrentScope(self.__dialogScope)
        self.__dialogScope = None
        if self.__timer > 0:
            self.__timerCallbackID = BigWorld.callback(1, self._timerCallback)
        return

    def _dispose(self):
        if self.__timerCallbackID is not None:
            BigWorld.cancelCallback(self.__timerCallbackID)
            self.__timerCallbackID = None
        if not self._isProcessed:
            self._callHandler(DIALOG_BUTTON_ID.CLOSE)
        self.__message = None
        self.__title = None
        self.__buttons = None
        self._handler = None
        self.__timer = None
        super(SimpleDialog, self)._dispose()
        return

    def onButtonClick(self, buttonID):
        self._callHandler(buttonID)
        self.destroy()

    def onWindowClose(self):
        self._callHandler(DIALOG_BUTTON_ID.CLOSE)
        self.destroy()

    def __setMessage(self):
        message = self.__message
        if self.__timer > 0:
            message = self.__message % {'time': self.__timer}
        self.as_setTextS(message)

    def _timerCallback(self):
        self.__timer -= 1
        if self.__timer > 0:
            self.__setMessage()
            self.__timerCallbackID = BigWorld.callback(1, self._timerCallback)
        else:
            self.onWindowClose()