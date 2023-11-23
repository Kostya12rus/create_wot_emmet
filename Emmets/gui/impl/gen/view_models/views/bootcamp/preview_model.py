# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/bootcamp/preview_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class PreviewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PreviewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)

    def _initialize(self):
        super(PreviewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addResourceProperty('description', R.invalid())