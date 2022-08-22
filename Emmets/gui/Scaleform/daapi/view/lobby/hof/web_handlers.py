# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hof/web_handlers.py
from web.web_client_api import webApiCollection, w2capi
from web.web_client_api.shop import ShopWebApi
from web.web_client_api.ui.browser import CloseBrowserViewWebApiMixin
from web.web_client_api.vehicles import VehiclesWebApi
from web.web_client_api.request import RequestWebApi
from web.web_client_api.sound import SoundWebApi
from web.web_client_api.ui import OpenWindowWebApi, OpenTabWebApi, ContextMenuWebApi

def createHofWebHandlers():

    @w2capi(name='close_window', key='window_id')
    class _CloseWindowWebApi(CloseBrowserViewWebApiMixin):
        pass

    return webApiCollection(_CloseWindowWebApi, OpenWindowWebApi, OpenTabWebApi, RequestWebApi, SoundWebApi, ContextMenuWebApi, ShopWebApi, VehiclesWebApi)