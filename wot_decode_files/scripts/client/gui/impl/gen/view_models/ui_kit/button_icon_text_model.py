# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/button_icon_text_model.py
from gui.impl.gen import R
from gui.impl.gen.view_models.ui_kit.button_common_model import ButtonCommonModel

class ButtonIconTextModel(ButtonCommonModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(ButtonIconTextModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getResource(6)

    def setIcon(self, value):
        self._setResource(6, value)

    def _initialize(self):
        super(ButtonIconTextModel, self)._initialize()
        self._addResourceProperty('icon', R.invalid())