# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/shop.py
from gui.shared import event_dispatcher
from gui.shared.event_dispatcher import hideWebBrowserOverlay
from web.web_client_api import w2c, W2CSchema, Field

class _OpenShopSchema(W2CSchema):
    path = Field(required=False, type=basestring)


class ShopWebApiMixin(object):

    @w2c(_OpenShopSchema, 'shop')
    def openShop(self, cmd):
        hideWebBrowserOverlay()
        event_dispatcher.showShop(path=cmd.path)