# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/constants/base_format_constants.py
from frameworks.wulf import ViewModel

class BaseFormatConstants(ViewModel):
    __slots__ = ()
    ALIGN_LEFT = 0
    ALIGN_RIGHT = 1
    ALIGN_CENTER = 4
    ALIGN_TOP = 0
    ALIGN_MIDDLE = 8
    ALIGN_BOTTOM = 2

    def __init__(self, properties=0, commands=0):
        super(BaseFormatConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(BaseFormatConstants, self)._initialize()