# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/platform/__init__.py
import typing
from constants import WGC_PUBLICATION
from helpers import dependency
from helpers.platform.base import BasePublishPlatform
from helpers.platform.steam import SteamPublishPlatform
from skeletons.gui.login_manager import ILoginManager
if typing.TYPE_CHECKING:
    from skeletons.helpers.platform import IPublishPlatform
_MAPPING = {WGC_PUBLICATION.WGC_STEAM: SteamPublishPlatform}

@dependency.replace_none_kwargs(loginManager=ILoginManager)
def getPublishPlatform(loginManager=None):
    pub = loginManager.getWgcPublication()
    if pub in _MAPPING:
        return _MAPPING[pub]()
    return BasePublishPlatform()