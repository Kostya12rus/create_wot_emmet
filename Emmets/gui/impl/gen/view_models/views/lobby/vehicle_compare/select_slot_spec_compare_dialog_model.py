# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/select_slot_spec_compare_dialog_model.py
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_content_model import SelectSlotSpecDialogContentModel
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class SelectSlotSpecCompareDialogModel(FullScreenDialogWindowModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=3):
        super(SelectSlotSpecCompareDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def mainContent(self):
        return self._getViewModel(11)

    @staticmethod
    def getMainContentType():
        return SelectSlotSpecDialogContentModel

    def _initialize(self):
        super(SelectSlotSpecCompareDialogModel, self)._initialize()
        self._addViewModelProperty('mainContent', SelectSlotSpecDialogContentModel())