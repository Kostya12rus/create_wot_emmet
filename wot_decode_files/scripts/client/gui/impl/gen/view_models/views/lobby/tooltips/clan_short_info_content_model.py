# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/clan_short_info_content_model.py
from frameworks.wulf import ViewModel

class ClanShortInfoContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ClanShortInfoContentModel, self).__init__(properties=properties, commands=commands)

    def getEmblem(self):
        return self._getString(0)

    def setEmblem(self, value):
        self._setString(0, value)

    def getFullName(self):
        return self._getString(1)

    def setFullName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(ClanShortInfoContentModel, self)._initialize()
        self._addStringProperty('emblem', '')
        self._addStringProperty('fullName', '')