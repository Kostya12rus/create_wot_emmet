# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/bootcamp/lobby/settings.py
from frameworks.wulf import WindowLayer, WindowFlags
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates
from gui.Scaleform.daapi.view.bootcamp.BCMessageWindow import BCMessageWindow
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.bootcamp.bootcamp_nation_view import BootcampNationView
from gui.impl.lobby.bootcamp.bootcamp_final_reward_view import BootcampFinalRewardView
BOOTCAMP_LOBBY_VIEW_SETTINGS = (
 GroupedViewSettings(VIEW_ALIAS.BOOTCAMP_MESSAGE_WINDOW, BCMessageWindow, 'BCMessageWindow.swf', WindowLayer.TOP_WINDOW, '', None, ScopeTemplates.TOP_WINDOW_SCOPE, canClose=False, canDrag=True, flags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN | WindowFlags.WINDOW_MODAL),)
DIALOG_ALIAS_MAP = {'bootcampMessage': VIEW_ALIAS.BOOTCAMP_MESSAGE_WINDOW, 
   'bootcampVideo': VIEW_ALIAS.BOOTCAMP_OUTRO_VIDEO}
WINDOW_ALIAS_MAP = {'bootcampSubtitle': VIEW_ALIAS.SUBTITLES_WINDOW}
GAMEFACE_ALIAS_MAP = {'bootcampSelectNation': BootcampNationView, 
   'bootcampFinalReward': BootcampFinalRewardView}