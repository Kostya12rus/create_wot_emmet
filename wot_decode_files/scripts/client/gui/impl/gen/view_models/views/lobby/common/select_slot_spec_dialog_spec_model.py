# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/select_slot_spec_dialog_spec_model.py
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_slot_model import SelectSlotSpecDialogSlotModel

class SelectSlotSpecDialogSpecModel(SelectSlotSpecDialogSlotModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SelectSlotSpecDialogSpecModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(SelectSlotSpecDialogSpecModel, self)._initialize()
        self._addNumberProperty('id', 0)