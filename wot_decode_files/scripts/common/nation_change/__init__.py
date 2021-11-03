# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/nation_change/__init__.py
from constants import ITEM_DEFS_PATH
from NationChangeSettings import NationChangeSettings
g_settings = None
PDATA_NATION_CHANGE_VEHICLE_DOSSIER_KEY = 'nationChangeVehicleDossier'
CONFIG_XML_PATH = ITEM_DEFS_PATH + 'nation_change.xml'
UNDEFINED_ID = -1

def init(settingsXml=CONFIG_XML_PATH):
    global g_settings
    g_settings = NationChangeSettings(settingsXml)


def findVehicleNationGroupId(vehicleTypeName):
    group = g_settings.findVehicleGroup(vehicleTypeName)
    if group is None:
        return UNDEFINED_ID
    else:
        return group.ID