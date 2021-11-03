# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/badge_model.py
from frameworks.wulf import ViewModel

class BadgeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BadgeModel, self).__init__(properties=properties, commands=commands)

    def getBadgeID(self):
        return self._getString(0)

    def setBadgeID(self, value):
        self._setString(0, value)

    def getLevel(self):
        return self._getString(1)

    def setLevel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(BadgeModel, self)._initialize()
        self._addStringProperty('badgeID', '')
        self._addStringProperty('level', '')