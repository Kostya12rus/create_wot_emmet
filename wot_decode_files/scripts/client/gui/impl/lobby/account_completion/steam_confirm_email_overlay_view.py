# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/steam_confirm_email_overlay_view.py
import typing
from gui.impl.backport import text as loc
from gui.impl.gen import R
from gui.impl.lobby.account_completion.common import errors
from gui.impl.lobby.account_completion.common.base_confirm_credentials_overlay_view import BaseConfirmCredentialsOverlayView
from gui.impl.lobby.account_completion.utils.common import showAccountAlreadyHasEmail
from gui.shared.event_dispatcher import showSteamAddEmailOverlay
from helpers import dependency
from skeletons.gui.platform.wgnp_controllers import IWGNPSteamAccRequestController
if typing.TYPE_CHECKING:
    from wg_async import _Future
    from gui.platform.wgnp.steam_account.request import ConfirmEmailParams as WGNPSAConfirmEmailParams
res = R.strings.dialogs.accountCompletion

class SteamConfirmEmailOverlayView(BaseConfirmCredentialsOverlayView):
    __slots__ = ()
    _wgnpSteamAccCtrl = dependency.descriptor(IWGNPSteamAccRequestController)

    def _getEmailAddedTime(self):
        return self._wgnpSteamAccCtrl.emailAddedTime

    def _doRequest(self):
        return self._wgnpSteamAccCtrl.confirmEmail(self._code.value)

    def _handleError(self, response):
        if response.isConfirmationCodeExpired:
            self._updateErrorModel(errorMessage=res.activate.keyDied(), buttonTimer=0)
        elif response.isConfirmationCodeDeactivated:
            self._updateErrorModel(errorMessage=errors.tooManyIncorrectTriesResID(), buttonTimer=0)
        elif response.isEmailAlreadyTaken:
            self._updateErrorModel(errorMessage=res.emailAlreadyTaken(), buttonTimer=0)
        elif response.isAccountAlreadyHasEmail:
            showAccountAlreadyHasEmail(self.viewModel)
        elif response.isConfirmationCodeIncorrect:
            self._updateErrorModel(errorMessage=errors.keyErrorResID())
        else:
            self._setWarning(loc(res.warningServerUnavailable()))

    def _onResend(self):
        showSteamAddEmailOverlay(initialEmail=self._email)