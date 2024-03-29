# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/crosshair/settings.py
import aih_constants
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS
CROSSHAIR_CONTAINER_SWF = 'battleCrosshairsApp.swf'
CROSSHAIR_ROOT_PATH = 'root.main'
CROSSHAIR_INIT_CALLBACK = ROOT_SWF_CONSTANTS.BATTLE_CROSSHAIRS_REGISTER_CALLBACK
CROSSHAIR_ITEM_PATH_FORMAT = '_level0.' + CROSSHAIR_ROOT_PATH + '.{}'
CROSSHAIR_RADIUS_MC_NAME = 'radiusMC'
SPG_GUN_MARKER_ELEMENTS_COUNT = aih_constants.SPG_GUN_MARKER_ELEMENTS_COUNT
SHOT_RESULT_TO_DEFAULT_COLOR = {aih_constants.SHOT_RESULT.UNDEFINED: 'normal', 
   aih_constants.SHOT_RESULT.NOT_PIERCED: 'red', 
   aih_constants.SHOT_RESULT.LITTLE_PIERCED: 'orange', 
   aih_constants.SHOT_RESULT.GREAT_PIERCED: 'green'}
SHOT_RESULT_TO_ALT_COLOR = {aih_constants.SHOT_RESULT.UNDEFINED: 'normal', 
   aih_constants.SHOT_RESULT.NOT_PIERCED: 'purple', 
   aih_constants.SHOT_RESULT.LITTLE_PIERCED: 'yellow', 
   aih_constants.SHOT_RESULT.GREAT_PIERCED: 'green'}