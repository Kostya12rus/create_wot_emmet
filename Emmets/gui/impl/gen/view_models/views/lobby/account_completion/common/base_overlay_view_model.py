# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/common/base_overlay_view_model.py
from frameworks.wulf import ViewModel

class BaseOverlayViewModel(ViewModel):
    __slots__ = ('onCloseClicked', 'onEscapePressed')

    def __init__(self, properties=2, commands=2):
        super(BaseOverlayViewModel, self).__init__(properties=properties, commands=commands)

    def getIsCloseVisible(self):
        return self._getBool(0)

    def setIsCloseVisible(self, value):
        self._setBool(0, value)

    def getIsHidden(self):
        return self._getBool(1)

    def setIsHidden(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(BaseOverlayViewModel, self)._initialize()
        self._addBoolProperty('isCloseVisible', True)
        self._addBoolProperty('isHidden', False)
        self.onCloseClicked = self._addCommand('onCloseClicked')
        self.onEscapePressed = self._addCommand('onEscapePressed')