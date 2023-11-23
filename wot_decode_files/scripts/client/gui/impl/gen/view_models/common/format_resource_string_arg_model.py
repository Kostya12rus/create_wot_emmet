# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/format_resource_string_arg_model.py
from frameworks.wulf import ViewModel

class FormatResourceStringArgModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FormatResourceStringArgModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(FormatResourceStringArgModel, self)._initialize()
        self._addStringProperty('value', '')
        self._addStringProperty('name', '')