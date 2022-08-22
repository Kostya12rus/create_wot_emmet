# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/base_modification_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BaseModificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BaseModificationModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getImageResName(self):
        return self._getString(1)

    def setImageResName(self, value):
        self._setString(1, value)

    def getTitleRes(self):
        return self._getResource(2)

    def setTitleRes(self, value):
        self._setResource(2, value)

    def getTooltipContentId(self):
        return self._getNumber(3)

    def setTooltipContentId(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(BaseModificationModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addStringProperty('imageResName', '')
        self._addResourceProperty('titleRes', R.invalid())
        self._addNumberProperty('tooltipContentId', 0)