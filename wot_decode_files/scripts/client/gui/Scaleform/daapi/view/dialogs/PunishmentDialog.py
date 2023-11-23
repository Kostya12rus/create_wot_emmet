# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/PunishmentDialog.py
from gui.Scaleform.daapi.view.meta.PunishmentDialogMeta import PunishmentDialogMeta

class PunishmentDialog(PunishmentDialogMeta):

    def __init__(self, meta, handler):
        super(PunishmentDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self.__msgTitle = meta.getMsgTitle()

    def _populate(self):
        super(PunishmentDialog, self)._populate()
        self.as_setMsgTitleS(self.__msgTitle)