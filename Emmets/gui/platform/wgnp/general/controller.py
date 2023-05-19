# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/wgnp/general/controller.py
import typing
from BWUtil import AsyncReturn
import wg_async
from gui.platform.base.statuses.controller_mixin import StatusesMixin
from gui.platform.wgnp.base.controller import WGNPRequestController
from gui.platform.wgnp.general.request import AccountCountryParams
from gui.platform.wgnp.general.statuses import GeneralAccountCountryStatus, createAccountCountryStatusFromResponse
from skeletons.gui.platform.wgnp_controllers import IWGNPGeneralRequestController
ACCOUNT_COUNTRY_CONTEXT = '<country>'

class WGNPGeneralRequestController(StatusesMixin, WGNPRequestController, IWGNPGeneralRequestController):

    @wg_async.wg_async
    def getAccountCountry(self, waitingID=None):
        status = self._getStatus(ACCOUNT_COUNTRY_CONTEXT)
        self._logger.debug('Getting account country from cache=%s, waitingID=%s.', status, waitingID)
        if status.isUndefined:
            response = yield self._request(AccountCountryParams(self.settings.getUrl()), waitingID=waitingID)
            status = createAccountCountryStatusFromResponse(response)
            self._updateStatus(status)
        raise AsyncReturn(status)