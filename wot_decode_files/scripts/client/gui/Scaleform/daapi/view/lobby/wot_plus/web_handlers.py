# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/web_handlers.py
import typing
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared.event_dispatcher import showHangar, showVehicleRentalPage
from web.web_client_api import Schema2Command
from web.web_client_api.ui import OpenTabWebApi
if typing.TYPE_CHECKING:
    from typing import Callable, Dict

class _OpenTabWebApi(OpenTabWebApi):

    def _getVehiclePreviewReturnAlias(self, cmd):
        return VIEW_ALIAS.WOT_PLUS_VEHICLE_PREVIEW

    def _getVehiclePreviewReturnCallback(self, cmd):
        return self.__getReturnCallback()

    def _getVehicleStylePreviewCallback(self, cmd):
        return self.__getReturnCallback()

    def __getReturnCallback(self):

        def _returnToVehicleRental():
            showHangar()
            showVehicleRentalPage()

        return _returnToVehicleRental


def getReplaceHandlers():
    return {'open_tab': _OpenTabWebApi}