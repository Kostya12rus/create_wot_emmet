# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/marathon/base_event_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BaseEventModel(ViewModel):
    __slots__ = ('onAction', )

    def __init__(self, properties=2, commands=1):
        super(BaseEventModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)

    def _initialize(self):
        super(BaseEventModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addResourceProperty('title', R.invalid())
        self.onAction = self._addCommand('onAction')