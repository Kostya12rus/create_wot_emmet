# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/CyberSportDialog.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class CyberSportDialog(SimpleDialog):

    def __init__(self, meta, handler):
        super(CyberSportDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), handler, meta.getViewScopeType())