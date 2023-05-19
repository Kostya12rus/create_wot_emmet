# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/StrongholdSendInvitesWindow.py
from functools import partial
from gui.prb_control.entities.base.external_battle_unit.base_external_battle_ctx import SendInvitesExternalBattleUnitCtx
from gui.Scaleform.daapi.view.lobby.SendInvitesWindow import SendInvitesWindow
from gui.shared.utils.requesters.abstract import Response
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper
from client_request_lib.exceptions import ResponseCodes
from gui import SystemMessages
from gui.Scaleform.locale.INVITES import INVITES

class StrongholdSendInvitesWindow(SendInvitesWindow, UsersInfoHelper):

    def sendInvites(self, accountsToInvite, comment):
        if accountsToInvite:
            self.prbEntity.request(SendInvitesExternalBattleUnitCtx(accountsToInvite, comment), partial(self.__sendInvitesCallback, accountsToInvite))

    def __sendInvitesCallback(self, accountsToInvite, response):
        if isinstance(response, Response) and response.getCode() == ResponseCodes.NO_ERRORS:
            for userId in accountsToInvite:
                SystemMessages.pushI18nMessage(INVITES.STRONGHOLD_INVITE_SENDINVITETOUSERNAME, type=SystemMessages.SM_TYPE.Information, name=self.getUserName(userId))