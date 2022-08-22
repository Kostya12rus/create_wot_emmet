# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/deserter_dialog.py
from gui.Scaleform.daapi.view.meta.DeserterDialogMeta import DeserterDialogMeta

class IngameDeserterDialog(DeserterDialogMeta):

    def __init__(self, meta, handler):
        super(IngameDeserterDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self.__imagePath = meta.getImagePath()
        self.__offsetY = meta.getOffsetY()

    def _populate(self):
        super(IngameDeserterDialog, self)._populate()
        self.as_setDataS(self.__imagePath, self.__offsetY)