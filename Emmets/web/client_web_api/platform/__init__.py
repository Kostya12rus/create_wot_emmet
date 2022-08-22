# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/platform/__init__.py
import typing
from helpers import dependency
from skeletons.helpers.platform import IPublishPlatform
from web.client_web_api.api import C2WHandler, c2w

class PlatformEventHandler(C2WHandler):
    __platform = dependency.descriptor(IPublishPlatform)

    def init(self):
        super(PlatformEventHandler, self).init()
        self.__platform.onPayment += self.__onPayment
        self.__platform.onOverlay += self.__onOverlay

    def fini(self):
        self.__platform.onPayment -= self.__onPayment
        self.__platform.onOverlay -= self.__onOverlay
        super(PlatformEventHandler, self).fini()

    @c2w(name='on_platform_payment')
    def __onPayment(self, orderID, authorized):
        return {'orderID': orderID, 
           'authorized': bool(authorized)}

    @c2w(name='on_overlay_activated')
    def __onOverlay(self, active):
        return {'isActive': active}