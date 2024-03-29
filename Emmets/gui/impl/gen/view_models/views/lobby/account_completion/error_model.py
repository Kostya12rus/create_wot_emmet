# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/error_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class ErrorModel(BaseOverlayViewModel):
    __slots__ = ('onButtonClicked', )

    def __init__(self, properties=5, commands=3):
        super(ErrorModel, self).__init__(properties=properties, commands=commands)

    def getTimer(self):
        return self._getNumber(2)

    def setTimer(self, value):
        self._setNumber(2, value)

    def getMessage(self):
        return self._getString(3)

    def setMessage(self, value):
        self._setString(3, value)

    def getButtonLabel(self):
        return self._getResource(4)

    def setButtonLabel(self, value):
        self._setResource(4, value)

    def _initialize(self):
        super(ErrorModel, self)._initialize()
        self._addNumberProperty('timer', 0)
        self._addStringProperty('message', '')
        self._addResourceProperty('buttonLabel', R.invalid())
        self.onButtonClicked = self._addCommand('onButtonClicked')