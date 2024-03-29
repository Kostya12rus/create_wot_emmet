# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/veh_post_progression/post_progression_intro.py
import typing
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS
from gui.impl.gen import R
from gui.impl.lobby.common.info_view import getInfoWindowProc
if typing.TYPE_CHECKING:
    from gui.impl.lobby.common.info_view import IInfoWindowProcessor

def getPostProgressionIntroWindowProc():
    return getInfoWindowProc(R.views.lobby.veh_post_progression.PostProgressionIntro(), uiStorageKey=UI_STORAGE_KEYS.POST_PROGRESSION_INTRO_SHOWN)


def getPostProgressionInfoWindowProc():
    return getInfoWindowProc(R.views.lobby.veh_post_progression.PostProgressionInfo())