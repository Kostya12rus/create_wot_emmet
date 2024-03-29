# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/text_button_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.ui_kit.button_common_model import ButtonCommonModel

class TextButtonModel(ButtonCommonModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(TextButtonModel, self).__init__(properties=properties, commands=commands)

    def getLabelAdditional(self):
        return self._getResource(6)

    def setLabelAdditional(self, value):
        self._setResource(6, value)

    def getLabelAdditionalString(self):
        return self._getString(7)

    def setLabelAdditionalString(self, value):
        self._setString(7, value)

    def getImage(self):
        return self._getResource(8)

    def setImage(self, value):
        self._setResource(8, value)

    def _initialize(self):
        super(TextButtonModel, self)._initialize()
        self._addResourceProperty('labelAdditional', R.invalid())
        self._addStringProperty('labelAdditionalString', '')
        self._addResourceProperty('image', R.invalid())