# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_presets/hangar_presets_getters.py
import typing
from constants import QUEUE_TYPE
from gui.hangar_presets.hangar_gui_helpers import ifComponentInPreset
from gui.Scaleform.genConsts.HANGAR_CONSTS import HANGAR_CONSTS
if typing.TYPE_CHECKING:
    from gui.hangar_presets.hangar_gui_config import HangarGuiPreset

class IPresetsGetter(object):

    def getPreset(self):
        raise NotImplementedError

    def getAmmoInjectViewAlias(self):
        raise NotImplementedError

    def getCarouselSettings(self):
        raise NotImplementedError


class BasePresetsGetter(IPresetsGetter):
    __slots__ = ('_presets', )
    _QUEUE_TYPE = None

    def __init__(self, config):
        self._presets = config.presets

    @ifComponentInPreset(HANGAR_CONSTS.AMMUNITION_INJECT)
    def getAmmoInjectViewAlias(self, preset=None):
        return preset.visibleComponents[HANGAR_CONSTS.AMMUNITION_INJECT].type

    @ifComponentInPreset(HANGAR_CONSTS.CAROUSEL)
    def getCarouselSettings(self, preset=None):
        component = preset.visibleComponents[HANGAR_CONSTS.CAROUSEL]
        return (component.type, component.layout)


class DefaultPresetsGetter(BasePresetsGetter):
    __slots__ = ('__presetName', )
    _QUEUE_TYPE = QUEUE_TYPE.RANDOMS

    def __init__(self, config):
        super(DefaultPresetsGetter, self).__init__(config)
        self.__presetName = config.modes.get(self._QUEUE_TYPE, QUEUE_TYPE.RANDOMS)

    def getPreset(self):
        return self._presets.get(self.__presetName)


class Comp7PresetsGetter(DefaultPresetsGetter):
    __slots__ = ()
    _QUEUE_TYPE = QUEUE_TYPE.COMP7


class MapboxPresetsGetter(DefaultPresetsGetter):
    __slots__ = ()
    _QUEUE_TYPE = QUEUE_TYPE.MAPBOX