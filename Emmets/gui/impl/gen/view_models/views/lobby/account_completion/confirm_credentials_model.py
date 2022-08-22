# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/confirm_credentials_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_field_model import BaseFieldModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel

class ConfirmCredentialsModel(BaseWgnpOverlayViewModel):
    __slots__ = ('onResendClicked', )

    def __init__(self, properties=13, commands=5):
        super(ConfirmCredentialsModel, self).__init__(properties=properties, commands=commands)

    @property
    def field(self):
        return self._getViewModel(9)

    @staticmethod
    def getFieldType():
        return BaseFieldModel

    def getTimer(self):
        return self._getNumber(10)

    def setTimer(self, value):
        self._setNumber(10, value)

    def getEmail(self):
        return self._getString(11)

    def setEmail(self, value):
        self._setString(11, value)

    def getResendButtonLabel(self):
        return self._getResource(12)

    def setResendButtonLabel(self, value):
        self._setResource(12, value)

    def _initialize(self):
        super(ConfirmCredentialsModel, self)._initialize()
        self._addViewModelProperty('field', BaseFieldModel())
        self._addNumberProperty('timer', 0)
        self._addStringProperty('email', '')
        self._addResourceProperty('resendButtonLabel', R.invalid())
        self.onResendClicked = self._addCommand('onResendClicked')