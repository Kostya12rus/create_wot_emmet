# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/ammunition_shells_section.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection

class AmmunitionShellsSection(AmmunitionItemsSection):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(AmmunitionShellsSection, self).__init__(properties=properties, commands=commands)

    def getInstalledCount(self):
        return self._getNumber(6)

    def setInstalledCount(self, value):
        self._setNumber(6, value)

    def getMaxCount(self):
        return self._getNumber(7)

    def setMaxCount(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(AmmunitionShellsSection, self)._initialize()
        self._addNumberProperty('installedCount', 0)
        self._addNumberProperty('maxCount', 0)