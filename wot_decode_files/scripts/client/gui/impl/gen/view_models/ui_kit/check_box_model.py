# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/check_box_model.py
from gui.impl.gen.view_models.ui_kit.button_common_model import ButtonCommonModel

class CheckBoxModel(ButtonCommonModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=2):
        super(CheckBoxModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CheckBoxModel, self)._initialize()