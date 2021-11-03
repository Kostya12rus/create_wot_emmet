# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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