# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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