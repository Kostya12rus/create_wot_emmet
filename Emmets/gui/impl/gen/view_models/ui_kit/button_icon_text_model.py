# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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