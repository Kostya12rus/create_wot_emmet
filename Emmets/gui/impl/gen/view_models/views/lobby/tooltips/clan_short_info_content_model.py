# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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