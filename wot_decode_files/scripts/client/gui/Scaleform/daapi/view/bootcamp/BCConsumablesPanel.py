# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCConsumablesPanel.py
from bootcamp.Bootcamp import g_bootcamp
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel
from gui.Scaleform.genConsts.CONSUMABLES_PANEL_SETTINGS import CONSUMABLES_PANEL_SETTINGS
from gui.impl.gen import R
R_EQUIPMENT_ICON_PATH_BIG = R.images.gui.maps.icons.artefact.big
R_EQUIPMENT_ICON_PATH_DEFAULT = R.images.gui.maps.icons.artefact

class BCConsumablesPanel(ConsumablesPanel):

    def __init__(self):
        super(BCConsumablesPanel, self).__init__()
        self.__isBigIcons = False

    def _populate(self):
        isBigIcons = g_bootcamp.checkBigConsumablesIconsLesson()
        if self.__isBigIcons != isBigIcons:
            self.__isBigIcons = isBigIcons
        super(BCConsumablesPanel, self)._populate()

    def _getPanelSettings(self):
        if self.__isBigIcons:
            return CONSUMABLES_PANEL_SETTINGS.BIG_SETTINGS_ID
        return super(BCConsumablesPanel, self)._getPanelSettings()

    def _getEquipmentIconPath(self, *_):
        if self.__isBigIcons:
            return R_EQUIPMENT_ICON_PATH_BIG
        return R_EQUIPMENT_ICON_PATH_DEFAULT

    def _addShellSlot(self, idx, intCD, descriptor, quantity, gunSettings):
        self._cds[idx] = intCD

    def _showEquipmentGlow(self, equipmentIndex, glowType=CONSUMABLES_PANEL_SETTINGS.GLOW_ID_ORANGE):
        if self.__isBigIcons:
            return
        super(BCConsumablesPanel, self)._showEquipmentGlow(equipmentIndex)