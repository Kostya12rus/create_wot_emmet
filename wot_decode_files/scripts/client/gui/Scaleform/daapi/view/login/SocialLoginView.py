# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/SocialLoginView.py
import BigWorld
from gui.login.social_networks import SOCIAL_NETWORKS
from LoginView import LoginView
from login_modes.social_mode import SOCIAL_NETWORK_TO_DOMAIN_MAPPING

class SocialLoginView(LoginView):

    def onRegister(self, host):
        self._loginMode.doSocialLogin(SOCIAL_NETWORKS.WGNI, host, True)

    def onLoginBySocial(self, socialNetworkName, serverName):
        self._loginMode.doSocialLogin(socialNetworkName, serverName, False)

    def onTextLinkClick(self, socialNetworkName):
        if socialNetworkName in SOCIAL_NETWORK_TO_DOMAIN_MAPPING:
            BigWorld.wg_openWebBrowser(SOCIAL_NETWORK_TO_DOMAIN_MAPPING[socialNetworkName])
            return
        super(SocialLoginView, self).onTextLinkClick(socialNetworkName)