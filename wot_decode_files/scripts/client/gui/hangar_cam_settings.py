# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cam_settings.py
from account_helpers.settings_core.options import HangarCamPeriodSetting
OPTIONS = HangarCamPeriodSetting.OPTIONS
HANGAR_CAM_PERIODS = {OPTIONS.TYPE0: 30, 
   OPTIONS.TYPE1: 45, 
   OPTIONS.TYPE2: 60}

def convertSettingToFeatures(value):
    selected = OPTIONS.HANGAR_CAM_TYPES[value]
    return HANGAR_CAM_PERIODS.get(selected, -1)