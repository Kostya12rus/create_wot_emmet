# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/browser_view_model.py
from gui.impl.gen.view_models.common.browser_model import BrowserModel

class BrowserViewModel(BrowserModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=7, commands=4):
        super(BrowserViewModel, self).__init__(properties=properties, commands=commands)

    def getIsClosable(self):
        return self._getBool(6)

    def setIsClosable(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(BrowserViewModel, self)._initialize()
        self._addBoolProperty('isClosable', False)
        self.onClose = self._addCommand('onClose')