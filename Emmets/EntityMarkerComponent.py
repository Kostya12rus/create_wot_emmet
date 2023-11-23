# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/EntityMarkerComponent.py
import typing
from script_component.DynamicScriptComponent import DynamicScriptComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.area_marker_ctrl import AreaMarkersController

class EntityMarkerComponent(DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(EntityMarkerComponent, self).__init__()
        self.markerID = None
        return

    def onDestroy(self):
        super(EntityMarkerComponent, self).onDestroy()
        ctrl = self.sessionProvider.shared.areaMarker
        ctrl.removeMarker(self.markerID)
        self.markerID = None
        return

    def _onAvatarReady(self):
        super(EntityMarkerComponent, self)._onAvatarReady()
        ctrl = self.sessionProvider.shared.areaMarker
        marker = ctrl.createMarker(self.entity.matrix, self.style)
        marker.setEntity(self.entity)
        self.markerID = ctrl.addMarker(marker)