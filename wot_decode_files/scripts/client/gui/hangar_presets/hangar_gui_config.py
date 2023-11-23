# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/hangar_gui_config.py
from collections import namedtuple
import typing
if typing.TYPE_CHECKING:
    from gui.hangar_presets.hangar_presets_reader import IPresetReader
_HANGAR_GUI_CONFIG = None
HangarGuiSettings = namedtuple('HangarGuiSettings', ('presets', 'modes'))
HangarGuiPreset = namedtuple('HangarGuiPreset', ('visibleComponents', 'hiddenComponents'))
PresetSettings = namedtuple('PresetSettings', ('type', 'layout', 'isChangeable'))

def _updateConfig(fullConfig, config):
    presets = {}
    presetsForQueueTypes = {}
    for c in [fullConfig, config]:
        presets.update(c.presets)
        presetsForQueueTypes.update(c.modes)

    return HangarGuiSettings(presets, presetsForQueueTypes)


def getHangarGuiConfig(readers):
    global _HANGAR_GUI_CONFIG
    if _HANGAR_GUI_CONFIG is None:
        fullConfig = HangarGuiSettings({}, {})
        for reader in readers:
            config = reader.readConfig(fullConfig)
            fullConfig = _updateConfig(fullConfig, config)

        _HANGAR_GUI_CONFIG = fullConfig
    return _HANGAR_GUI_CONFIG