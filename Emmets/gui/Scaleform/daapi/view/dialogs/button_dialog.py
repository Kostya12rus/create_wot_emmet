# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/button_dialog.py
from SimpleDialog import SimpleDialog

class ButtonDialog(SimpleDialog):

    def _callHandler(self, buttonID):
        if self._handler is not None:
            self._handler(buttonID)
            self._isProcessed = True
        return