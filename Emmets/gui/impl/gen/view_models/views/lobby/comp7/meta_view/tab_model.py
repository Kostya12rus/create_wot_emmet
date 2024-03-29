# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/tab_model.py
from enum import IntEnum
from frameworks.wulf import ViewModel

class Tabs(IntEnum):
    PROGRESSION = 0
    RANKREWARDS = 1
    WEEKLYQUESTS = 2
    LEADERBOARD = 3


class TabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(TabModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return Tabs(self._getNumber(0))

    def setName(self, value):
        self._setNumber(0, value.value)

    def _initialize(self):
        super(TabModel, self)._initialize()
        self._addNumberProperty('name')