# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/debug_ctrl.py
import BigWorld, BattleReplay
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController
from gui.shared.utils.TimeInterval import TimeInterval
from helpers import dependency
from skeletons.helpers.statistics import IStatisticsCollector
_UPDATE_INTERVAL = 0.2

class IDebugPanel(object):

    def updateDebugInfo(self, ping, fps, isLaggingNow, fpsReplay):
        raise NotImplementedError


class DebugController(IViewComponentsController):
    statsCollector = dependency.descriptor(IStatisticsCollector)

    def __init__(self):
        super(DebugController, self).__init__()
        self._debugPanelUI = None
        self._timeInterval = None
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.DEBUG

    def startControl(self):
        self._timeInterval = TimeInterval(_UPDATE_INTERVAL, self, '_update')
        self._timeInterval.start()

    def stopControl(self):
        self._timeInterval.stop()
        self._timeInterval = None
        self.clearViewComponents()
        return

    def setViewComponents(self, debugPanelUI):
        self._debugPanelUI = debugPanelUI

    def clearViewComponents(self):
        self._debugPanelUI = None
        return

    def _update(self):
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying:
            fps = BigWorld.getFPS()[1]
            fpsReplay = replayCtrl.fps
            ping = replayCtrl.ping
            isLaggingNow = replayCtrl.isLaggingNow
        else:
            fpsReplay = -1
            isLaggingNow = BigWorld.statLagDetected()
            ping = BigWorld.statPing()
            fps = BigWorld.getFPS()[1]
            self.statsCollector.update()
            if replayCtrl.isRecording:
                replayCtrl.setFpsPingLag(fps, ping, isLaggingNow)
            try:
                ping = int(ping)
                fps = int(fps)
                fpsReplay = int(fpsReplay)
            except (ValueError, OverflowError):
                return

        if self._debugPanelUI is not None:
            self._debugPanelUI.updateDebugInfo(ping, fps, isLaggingNow, fpsReplay)
        return