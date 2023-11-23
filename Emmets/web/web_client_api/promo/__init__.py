# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/promo/__init__.py
from helpers import dependency
from skeletons.gui.game_control import IPromoController
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _PromoCountSchema(W2CSchema):
    count = Field(required=True, type=int)


@w2capi(name='promo', key='action')
class PromoWebApi(object):
    _promoCtrl = dependency.descriptor(IPromoController)

    @w2c(_PromoCountSchema, 'unread_count')
    def promoCount(self, cmd):
        self._promoCtrl.setUnreadPromoCount(cmd.count)