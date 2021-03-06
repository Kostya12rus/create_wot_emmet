# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/components/new_year_tab_model.py
from frameworks.wulf import ViewModel

class NewYearTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NewYearTabModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getUnseenCount(self):
        return self._getNumber(1)

    def setUnseenCount(self, value):
        self._setNumber(1, value)

    def getInfoCount(self):
        return self._getNumber(2)

    def setInfoCount(self, value):
        self._setNumber(2, value)

    def getIconName(self):
        return self._getString(3)

    def setIconName(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(NewYearTabModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addNumberProperty('unseenCount', 0)
        self._addNumberProperty('infoCount', 0)
        self._addStringProperty('iconName', '')