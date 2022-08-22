# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/SystemMessageDialog.py
from gui.Scaleform.daapi.view.meta.SystemMessageDialogMeta import SystemMessageDialogMeta

class SystemMessageDialog(SystemMessageDialogMeta):

    def __init__(self, meta, handler):
        super(SystemMessageDialog, self).__init__()
        self.__meta = meta
        self.__handler = handler

    def _populate(self):
        super(SystemMessageDialog, self)._populate()
        self.as_setInitDataS({'title': self.__meta.getTitle(), 
           'closeBtnTitle': self.__meta.getCancelLabel(), 
           'settings': self.__meta.getSettings()})
        self.as_setMessageDataS(self.__meta.getMessageObject())

    def onWindowClose(self):
        self.destroy()

    def _dispose(self):
        if self.__handler:
            self.__handler(True)
        self.__meta.cleanUp()
        self.__meta = None
        self.__handler = None
        super(SystemMessageDialog, self)._dispose()
        return