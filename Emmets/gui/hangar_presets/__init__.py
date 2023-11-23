# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/__init__.py
from constants import QUEUE_TYPE
from gui.hangar_presets.hangar_presets_reader import DefaultPresetReader, SpecBattlePresetReader
from gui.hangar_presets.hangar_presets_getters import DefaultPresetsGetter, Comp7PresetsGetter, MapboxPresetsGetter, SpecBattlePresetsGetter
from gui.shared.system_factory import registerHangarPresetsReader, registerHangarPresetGetter
registerHangarPresetsReader(DefaultPresetReader)
registerHangarPresetsReader(SpecBattlePresetReader)
registerHangarPresetGetter(QUEUE_TYPE.RANDOMS, DefaultPresetsGetter)
registerHangarPresetGetter(QUEUE_TYPE.MAPBOX, MapboxPresetsGetter)
registerHangarPresetGetter(QUEUE_TYPE.COMP7, Comp7PresetsGetter)
registerHangarPresetGetter(QUEUE_TYPE.SPEC_BATTLE, SpecBattlePresetsGetter)