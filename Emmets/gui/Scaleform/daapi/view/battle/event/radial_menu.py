# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/radial_menu.py
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES, MarkerType, DefaultMarkerSubType
from gui.Scaleform.genConsts.RADIAL_MENU_CONSTS import RADIAL_MENU_CONSTS
from gui.Scaleform.locale.INGAME_HELP import INGAME_HELP
from gui.Scaleform.daapi.view.battle.shared import radial_menu
_CAN_CANCEL_REPLY_SHORTCUT = radial_menu.Shortcut(title=INGAME_HELP.EVENTRADIALMENU_CANCEL, action=BATTLE_CHAT_COMMAND_NAMES.CANCEL_REPLY, icon=RADIAL_MENU_CONSTS.EVENT_CANCEL, groups=[
 RADIAL_MENU_CONSTS.TARGET_STATE_EVENT_CAMP, RADIAL_MENU_CONSTS.TARGET_STATE_EVENT_COLLECTOR], bState=RADIAL_MENU_CONSTS.NORMAL_BUTTON_STATE, indexInGroup=RADIAL_MENU_CONSTS.ELEMENT_INDEX_FIRST)
_MARKERS_TYPE_TO_SUBTYPE_MAP = {MarkerType.BASE_MARKER_TYPE: {DefaultMarkerSubType.ALLY_MARKER_SUBTYPE: RADIAL_MENU_CONSTS.TARGET_STATE_EVENT_COLLECTOR, 
                                 DefaultMarkerSubType.ENEMY_MARKER_SUBTYPE: RADIAL_MENU_CONSTS.TARGET_STATE_EVENT_CAMP}}

class EventRadialMenu(radial_menu.RadialMenu):

    def _getCanCancelReplyShortcut(self):
        return _CAN_CANCEL_REPLY_SHORTCUT

    def _getSubtypeMapByMarkersType(self, targetMarkerType):
        if targetMarkerType in _MARKERS_TYPE_TO_SUBTYPE_MAP:
            return _MARKERS_TYPE_TO_SUBTYPE_MAP[targetMarkerType]
        return radial_menu.MARKERS_TYPE_TO_SUBTYPE_MAP[targetMarkerType]