# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/__init__.py
import typing
from gui import GUI_SETTINGS
from skeletons.gui.login_manager import ILoginManager
from helpers import dependency
from wgc_mode import WgcMode
from steam_mode import SteamMode
from credentials_mode import CredentialsMode
from social_mode import SocialMode
if typing.TYPE_CHECKING:
    from base_mode import BaseMode

@dependency.replace_none_kwargs(loginManager=ILoginManager)
def createLoginMode(view, loginManager=None):
    if loginManager.isWgcSteam:
        return SteamMode(view)
    mode = CredentialsMode(view)
    if GUI_SETTINGS.socialNetworkLogin['enabled']:
        mode = SocialMode(view, mode)
    if loginManager.wgcAvailable:
        mode = WgcMode(view, mode)
    return mode