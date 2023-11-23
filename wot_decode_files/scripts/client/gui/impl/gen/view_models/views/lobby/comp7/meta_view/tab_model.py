# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/tab_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class MetaRootViews(IntEnum):
    PROGRESSION = 0
    RANKREWARDS = 1
    WEEKLYQUESTS = 2
    LEADERBOARD = 3


class TabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TabModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return MetaRootViews(self._getNumber(0))

    def setId(self, value):
        self._setNumber(0, value.value)

    def getHasNotification(self):
        return self._getBool(1)

    def setHasNotification(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(TabModel, self)._initialize()
        self._addNumberProperty('id')
        self._addBoolProperty('hasNotification', False)