# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/loading.py
import inspect, typing, WWISE, game_loading_bindings
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.game_loading import loggers
from gui.game_loading.preferences import GameLoadingPreferences
from gui.game_loading.settings import GameLoadingSettings
from gui.game_loading.state_machine.machine import GameLoadingStateMachine
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
_logger = loggers.getLoaderLogger()
_g_Loader = GameLoadingStateMachine()

def startSound():
    WWISE.WG_loadLogin()
    WWISE.WW_eventGlobalSync('ue_01_loginscreen_enter')
    WWISE.WW_eventGlobal('loginscreen_ambient_start')


def getLoader():
    return _g_Loader


def tick(stepNumber):
    getLoader().tick(stepNumber)


def initialize(preferences, settings):
    try:
        settings = GameLoadingSettings(settings)
        preferences = GameLoadingPreferences(preferences)
        _g_Loader.configure(preferences, settings)
        _g_Loader.start()
    except Exception:
        LOG_CURRENT_EXCEPTION()


def step():
    if game_loading_bindings.getIsVerbose():
        stackList = inspect.stack()
        if len(stackList) >= 1:
            currentFrame = stackList[1]
            if len(currentFrame) >= 4:
                _logger.info('[game_loading] %s %s : %s', currentFrame[1], currentFrame[3], currentFrame[2])
    game_loading_bindings.step()