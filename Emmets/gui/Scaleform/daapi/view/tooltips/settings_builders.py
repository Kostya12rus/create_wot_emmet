# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/settings_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import common
from gui.shared.tooltips.builders import DataBuilder, DefaultFormatBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DefaultFormatBuilder(TOOLTIPS_CONSTANTS.SETTINGS_CONTROL, TOOLTIPS_CONSTANTS.COMPLEX_UI, common.SettingsControlTooltipData(contexts.HangarContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_BUTTON, TOOLTIPS_CONSTANTS.SETTINGS_BUTTON_UI, common.SettingsButtonTooltipData(contexts.HangarServerStatusContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_MINIMAP_CIRCLES, TOOLTIPS_CONSTANTS.SETTINGS_MINIMAP_CIRCLES_UI, common.SettingsMinimapCircles(contexts.SettingsMinimapContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_KEY_SWITCH_MODE, TOOLTIPS_CONSTANTS.SETTINGS_KEY_SWITCH_MODE_UI, common.SettingKeySwitchMode(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_KEY_HIGHLIGHTLOCATION, TOOLTIPS_CONSTANTS.SETTINGS_KEY_HIGHLIGHTLOCATION_UI, common.SettingsKeyHighlightLocation(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_KEY_HIGHLIGHTTARGET, TOOLTIPS_CONSTANTS.SETTINGS_KEY_HIGHLIGHTTARGET_UI, common.SettingsKeyHighlightTarget(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_KEY_SHOWRADIALMENU, TOOLTIPS_CONSTANTS.SETTINGS_KEY_SHOWRADIALMENU_UI, common.SettingsKeyShowRadialMenu(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_SHOW_LOCATION_MARKERS, TOOLTIPS_CONSTANTS.SETTINGS_SHOW_LOCATION_MARKERS_UI, common.SettingsShowLocationMarkers(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_KEY_CHARGE_FIRE, TOOLTIPS_CONSTANTS.SETTINGS_KEY_CHARGE_FIRE_UI, common.SettingsKeyChargeFire(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.SETTINGS_SWITCH_EQUIPMENT, TOOLTIPS_CONSTANTS.SETTINGS_SWITCH_EQUIPMENT_UI, common.SettingsSwitchEquipment(contexts.ToolTipContext(None))))