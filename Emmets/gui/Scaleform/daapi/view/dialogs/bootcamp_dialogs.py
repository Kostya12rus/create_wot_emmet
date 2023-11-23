# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/bootcamp_dialogs.py
from gui.Scaleform.daapi.view.meta.BootcampDialogMeta import BootcampDialogMeta

class ExecutionChooserDialog(BootcampDialogMeta):

    def __init__(self, meta, handler):
        super(ExecutionChooserDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self.__imagePath = meta.getImagePath()
        self.__label = meta.getLabel()
        self.__showAwardIcon = meta.getShowAwardIcon()
        self.__awardingText = meta.getAwardingText()

    def _populate(self):
        super(ExecutionChooserDialog, self)._populate()
        self.as_setDataS(self.__imagePath, self.__label, self.__showAwardIcon, self.__awardingText)