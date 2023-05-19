# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/constants.py
from gui.Scaleform.genConsts.POI_CONSTS import POI_CONSTS
from points_of_interest_shared import PoiStatus, PoiType
POI_TYPE_UI_MAPPING = {PoiType.ARTILLERY: POI_CONSTS.POI_TYPE_ARTILLERY, 
   PoiType.RECON: POI_CONSTS.POI_TYPE_RECON}
POI_STATUS_UI_MAPPING = {PoiStatus.ACTIVE: POI_CONSTS.POI_STATUS_ACTIVE, 
   PoiStatus.CAPTURING: POI_CONSTS.POI_STATUS_CAPTURING, 
   PoiStatus.COOLDOWN: POI_CONSTS.POI_STATUS_COOLDOWN}