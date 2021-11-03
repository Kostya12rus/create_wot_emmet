# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/squad_action_button_state_vo.py
from gui.Scaleform.daapi.view.lobby.rally.action_button_state_vo import ActionButtonStateVO
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.prb_control.settings import UNIT_RESTRICTION
_VALID_RESTRICTIONS = (
 UNIT_RESTRICTION.COMMANDER_VEHICLE_NOT_SELECTED,
 UNIT_RESTRICTION.NOT_READY_IN_SLOTS,
 UNIT_RESTRICTION.UNIT_NOT_FULL)

class SquadActionButtonStateVO(ActionButtonStateVO):

    def _isEnabled(self, isValid, restriction):
        return isValid or restriction in _VALID_RESTRICTIONS

    def _getLabel(self):
        if self._playerInfo.isReady:
            label = CYBERSPORT.WINDOW_UNIT_NOTREADY
        else:
            label = CYBERSPORT.WINDOW_UNIT_READY
        return label

    def _getArenaStateStr(self):
        return (
         CYBERSPORT.WINDOW_UNIT_MESSAGE_SQUADINBATTLE, {})

    def _getReadyValidInSlotStateStr(self):
        return (
         CYBERSPORT.WINDOW_UNIT_MESSAGE_GETNOTREADY, {})

    def _getIdleStateStr(self):
        return (
         CYBERSPORT.SQUADWINDOW_WAITINGFORBATTLE, {})