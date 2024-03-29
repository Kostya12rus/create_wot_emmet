# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/base/controller.py
import typing, wg_async
from BWUtil import AsyncReturn
from gui.platform.base.controller import PlatformRequestController
from gui.platform.base.settings import REQUEST_TIMEOUT
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.platform.wgnp_controllers import IWGNPRequestController
if typing.TYPE_CHECKING:
    from gui.platform.base.request import Params
    from helpers.server_settings import _Wgnp

class WGNPRequestController(PlatformRequestController, IWGNPRequestController):
    lobbyContext = dependency.descriptor(ILobbyContext)

    @property
    def settings(self):
        return self.lobbyContext.getServerSettings().wgnp

    @wg_async.wg_async
    def _request(self, params, timeout=REQUEST_TIMEOUT, waitingID=None):
        if not self.settings.isEnabled():
            self._logger.debug('WGNP disabled.')
            response = params.response.createServiceDisabled()
        else:
            response = yield super(WGNPRequestController, self)._request(params, timeout=timeout, waitingID=waitingID)
        raise AsyncReturn(response)