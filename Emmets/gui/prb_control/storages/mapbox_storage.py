# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/mapbox_storage.py
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IMapboxController

class MapboxStorage(SessionStorage):
    __mapboxCtrl = dependency.descriptor(IMapboxController)

    def isModeSelected(self):
        isMapboxAvailable = self.__mapboxCtrl.isEnabled() and self.__mapboxCtrl.getCurrentSeason() is not None
        return super(MapboxStorage, self).isModeSelected() and isMapboxAvailable

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isMapbox()