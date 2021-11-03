# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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