# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_columns.py
from frameworks.wulf import ViewModel

class ModeSelectorColumns(ViewModel):
    __slots__ = ()
    COLUMN_0 = 0
    COLUMN_1 = 1
    COLUMN_2 = 2
    COLUMN_3 = 3

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorColumns, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ModeSelectorColumns, self)._initialize()