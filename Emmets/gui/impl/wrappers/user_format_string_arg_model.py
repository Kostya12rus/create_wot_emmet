# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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