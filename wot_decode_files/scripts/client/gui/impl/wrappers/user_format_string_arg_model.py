# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/wrappers/user_format_string_arg_model.py
from gui.impl.gen.view_models.common.format_string_arg_model import FormatStringArgModel

class UserFormatStringArgModel(FormatStringArgModel):
    __slots__ = ()

    def __init__(self, value, name='', style=None, align=FormatStringArgModel.ALIGN_LEFT, hardSpace=False):
        super(UserFormatStringArgModel, self).__init__()
        self.setValue(value)
        self.setName(name)
        self.setAlign(align)
        self.setHardSpace(hardSpace)
        if style is not None:
            self.setStyle(style)
        return