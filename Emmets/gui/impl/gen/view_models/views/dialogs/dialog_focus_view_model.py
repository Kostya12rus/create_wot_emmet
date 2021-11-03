# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/dialog_focus_view_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_base_focus_view_model import DialogBaseFocusViewModel

class DialogFocusViewModel(DialogBaseFocusViewModel):
    __slots__ = ('onTabPressed', )
    NOT_FOCUSED_INDEX = -1
    DEFAULT_FOCUSED_INDEX = 0

    def __init__(self, properties=1, commands=1):
        super(DialogFocusViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DialogFocusViewModel, self)._initialize()
        self.onTabPressed = self._addCommand('onTabPressed')