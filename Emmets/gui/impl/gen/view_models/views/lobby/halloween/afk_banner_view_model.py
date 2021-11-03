# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/halloween/afk_banner_view_model.py
from frameworks.wulf import ViewModel

class AfkBannerViewModel(ViewModel):
    __slots__ = ()
    AFK_BANNER_TOOLTIP_ID = 'eventBanInfo'

    def __init__(self, properties=2, commands=0):
        super(AfkBannerViewModel, self).__init__(properties=properties, commands=commands)

    def getIsAfk(self):
        return self._getBool(0)

    def setIsAfk(self, value):
        self._setBool(0, value)

    def getAfkTimer(self):
        return self._getString(1)

    def setAfkTimer(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(AfkBannerViewModel, self)._initialize()
        self._addBoolProperty('isAfk', False)
        self._addStringProperty('afkTimer', '')