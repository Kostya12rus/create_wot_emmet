# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/select_slot_spec_dialog_slot_model.py
from frameworks.wulf import ViewModel

class SelectSlotSpecDialogSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SelectSlotSpecDialogSlotModel, self).__init__(properties=properties, commands=commands)

    def getSpecialization(self):
        return self._getString(0)

    def setSpecialization(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(SelectSlotSpecDialogSlotModel, self)._initialize()
        self._addStringProperty('specialization', '')