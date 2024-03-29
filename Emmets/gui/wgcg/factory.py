# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/factory.py
import BigWorld
from client_request_lib.requester import Requester as WebRequester
from constants import TOKEN_TYPE
from gui.shared.utils.requesters import TokenRequester, getTokenRequester
from gui.wgcg.requests import WgcgRequester, WgcgRequestsController
from helpers.server_settings import _Wgcg

def _webUrlFetcher(url, callback, headers=None, timeout=30.0, method='GET', postData=''):
    return BigWorld.fetchURL(url, callback, headers, timeout, method, postData)


class _WebFactory(object):

    def createWebRequester(self, settings, *args, **kwargs):
        raise NotImplementedError

    def createTokenRequester(self):
        raise NotImplementedError

    def createWgcgRequester(self, webRequester):
        raise NotImplementedError

    def createWgcgRequestsController(self, webCtrl, clanRequester):
        raise NotImplementedError


class WebFactory(_WebFactory):

    def createWebRequester(self, settings, *args, **kwargs):
        return WebRequester.create_requester(_webUrlFetcher, settings, *args, **kwargs)

    def createTokenRequester(self):
        return getTokenRequester(TOKEN_TYPE.WGNI_JWT)

    def createWgcgRequester(self, webRequester):
        return WgcgRequester(webRequester)

    def createWgcgRequestsController(self, webCtrl, clanRequester):
        return WgcgRequestsController(webCtrl, clanRequester)


class FakeWebFactory(_WebFactory):

    def createWebRequester(self, settings, *args, **kwargs):
        return WebRequester.create_requester(_webUrlFetcher, _Wgcg(True, None, 'fake', False, False), *args, **kwargs)

    def createTokenRequester(self):
        return TokenRequester(TOKEN_TYPE.WGNI, cache=False)

    def createWgcgRequester(self, webRequester):
        return WgcgRequester(webRequester)

    def createWgcgRequestsController(self, webCtrl, clanRequester):
        return WgcgRequestsController(webCtrl, clanRequester)


g_webFactory = WebFactory()