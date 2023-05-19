# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/miniclient/lobby/__init__.py
from gui.miniclient.lobby.user_cm_handlers import UserCmClanUnavailablePointCut, UserCmInviteClanUnavailablePointCut
import tank_carousel
from hangar import configure_pointcuts as _configure_hangar_pointcuts
from header import configure_pointcuts as _configure_header_pointcuts
from tank_carousel import configure_pointcuts as _configure_carousel_pointcuts
from profile import configure_pointcuts as _configure_profile_pointcuts
from strongholds import configure_pointcuts as _configure_strongholds_pointcuts
from MiniclientDescriptionWindow import MiniclientDescriptionWindow

def configure_pointcuts(config):
    _configure_carousel_pointcuts(config)
    _configure_hangar_pointcuts(config)
    _configure_header_pointcuts(config)
    _configure_profile_pointcuts()
    _configure_strongholds_pointcuts()
    MiniclientDescriptionWindow()
    UserCmClanUnavailablePointCut()
    UserCmInviteClanUnavailablePointCut()