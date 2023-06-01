# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/styles_perf_toolset/styles_overrider.py
import logging, ResMgr
from items.vehicles import makeIntCompactDescrByID, getItemByCompactDescr
from items.components.c11n_constants import CustomizationType, SeasonType

class StylesOverrider(object):

    def __init__(self):
        self.__stylesConfig = {}

    @property
    def stylesConfig(self):
        return self.__stylesConfig

    def loadStylesConfig(self, configPath):
        section = ResMgr.openSection(configPath, False)
        if section is None:
            logging.error('failed to open styles configuration file: %s', configPath)
            return
        else:
            for value in section.values():
                name = value.readString('name', '')
                style = value.readInt('style', -1)
                if name != '' and style != -1:
                    self.__stylesConfig[name] = style

            return

    def overrideStyleForVehicle(self, vehicleName):
        if vehicleName in self.__stylesConfig:
            style = self.__stylesConfig[vehicleName]
            styleItem = getItemByCompactDescr(makeIntCompactDescrByID('customizationItem', CustomizationType.STYLE, style))
            outfitDescr = styleItem.outfits[SeasonType.SUMMER].makeCompDescr()
            return outfitDescr
        else:
            return