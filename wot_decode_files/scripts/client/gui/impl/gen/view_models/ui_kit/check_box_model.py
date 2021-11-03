# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/ui_kit/check_box_model.py
from gui.impl.gen.view_models.ui_kit.button_common_model import ButtonCommonModel

class CheckBoxModel(ButtonCommonModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=2):
        super(CheckBoxModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CheckBoxModel, self)._initialize()