# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wgnc/WGNCDialog.py
from gui.Scaleform.daapi.view.meta.WGNCDialogMeta import WGNCDialogMeta
from gui.wgnc import g_wgncProvider

class WGNCDialog(WGNCDialogMeta):

    def __init__(self, ctx=None):
        super(WGNCDialog, self).__init__()
        self.__notID = ctx['notID']
        self.__target = ctx['target']

    def onWindowClose(self):
        self.destroy()

    def doAction(self, actionID, isButtonClicked):
        g_wgncProvider.doAction(self.__notID, actionID, self.__target)
        if isButtonClicked:
            self.destroy()

    def _populate(self):
        super(WGNCDialog, self)._populate()
        item = g_wgncProvider.getNotItemByName(self.__notID, self.__target)
        self.as_setTextS(item.getBody())
        self.as_setTitleS(item.getTopic())
        self.as_setButtonsS(item.getButtonsMap())

    def _dispose(self):
        self.__notID = None
        self.__target = None
        super(WGNCDialogMeta, self)._dispose()
        return