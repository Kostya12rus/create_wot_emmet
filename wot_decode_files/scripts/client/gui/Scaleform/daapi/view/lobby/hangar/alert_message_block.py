# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/alert_message_block.py
from gui.Scaleform.daapi.view.meta.AlertMessageBlockMeta import AlertMessageBlockMeta

class AlertMessageBlock(AlertMessageBlockMeta):

    def __init__(self):
        super(AlertMessageBlock, self).__init__()
        self.__onBtnClickCallback = None
        return

    def update(self, alertMsgData, onBtnClickCallback=None):
        self.__onBtnClickCallback = onBtnClickCallback
        self.as_setDataS(alertMsgData)

    def onButtonClick(self):
        if self.__onBtnClickCallback:
            self.__onBtnClickCallback()

    def _dispose(self):
        super(AlertMessageBlock, self)._dispose()
        self.__onBtnClickCallback = None
        return