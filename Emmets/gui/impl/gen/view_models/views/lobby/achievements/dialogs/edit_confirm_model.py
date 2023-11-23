# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/dialogs/edit_confirm_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class DialogType(Enum):
    AUTO_SELECT_ENABLED = 'autoSelectEnabled'
    AUTO_SELECT_DISABLED = 'autoSelectDisabled'
    ERROR = 'error'


class EditConfirmModel(ViewModel):
    __slots__ = ('onAccept', 'onCancel', 'onClose')

    def __init__(self, properties=1, commands=3):
        super(EditConfirmModel, self).__init__(properties=properties, commands=commands)

    def getDialogType(self):
        return DialogType(self._getString(0))

    def setDialogType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(EditConfirmModel, self)._initialize()
        self._addStringProperty('dialogType')
        self.onAccept = self._addCommand('onAccept')
        self.onCancel = self._addCommand('onCancel')
        self.onClose = self._addCommand('onClose')