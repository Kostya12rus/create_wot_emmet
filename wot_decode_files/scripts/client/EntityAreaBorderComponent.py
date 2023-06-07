# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/EntityAreaBorderComponent.py
import BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent
from account_helpers.settings_core import ISettingsCore, settings_constants
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent

class EntityAreaBorderComponent(DynamicScriptComponent):
    DRAW_TYPE_NORMAL = 0
    COLOR_BLINDNESS_MATERIAL_PARAM_NAME = 'g_isColorBlind'
    STRIPES_ENABLED_MATERIAL_PARAM_NAME = 'g_stripesEnabled'
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(EntityAreaBorderComponent, self).__init__()
        self._border = None
        return

    def onDestroy(self):
        super(EntityAreaBorderComponent, self).onDestroy()
        self.settingsCore.onSettingsChanged -= self._onSettingsChanged
        g_eventBus.removeListener(GameEvent.ARENA_BORDER_TYPE_CHANGED, self._onArenaBorderTypeChanged, scope=EVENT_BUS_SCOPE.BATTLE)
        self._border = None
        return

    def set_isVisible(self, oldValue):
        self.updateBorderVisibility()

    @property
    def isBorderVisible(self):
        return self.isVisible

    def updateBorderVisibility(self):
        if not self._border:
            return
        self._border.setVisibility(self.isBorderVisible)

    def updateColorBlindness(self):
        isColorBlind = self.settingsCore.getSetting(settings_constants.GRAPHICS.COLOR_BLIND)
        self._border.setMaterialBoolParam(self.COLOR_BLINDNESS_MATERIAL_PARAM_NAME, isColorBlind)

    def getClosestPoint(self, pos, searchRadius):
        if self._border:
            return self._border.getClosestPoint(pos, searchRadius)
        else:
            return

    def updateDrawStyle(self):
        arenaBorderCtrl = self.sessionProvider.shared.arenaBorder
        if arenaBorderCtrl:
            stripesEnabled = arenaBorderCtrl.getDrawType() == self.DRAW_TYPE_NORMAL
            self._border.setMaterialBoolParam(self.STRIPES_ENABLED_MATERIAL_PARAM_NAME, stripesEnabled)

    def _onAvatarReady(self):
        super(EntityAreaBorderComponent, self)._onAvatarReady()
        self.settingsCore.onSettingsChanged += self._onSettingsChanged
        udo = BigWorld.userDataObjects.get(self.udoGuid, None)
        if udo is None:
            return
        else:
            self._border = BigWorld.PolygonalAreaBorder(self.spaceID, self.udoGuid)
            self.updateBorderVisibility()
            self.updateColorBlindness()
            self.updateDrawStyle()
            g_eventBus.addListener(GameEvent.ARENA_BORDER_TYPE_CHANGED, self._onArenaBorderTypeChanged, scope=EVENT_BUS_SCOPE.BATTLE)
            return

    def _onSettingsChanged(self, diff):
        if settings_constants.GRAPHICS.COLOR_BLIND in diff:
            self.updateColorBlindness()

    def _onArenaBorderTypeChanged(self, event):
        self.updateDrawStyle()