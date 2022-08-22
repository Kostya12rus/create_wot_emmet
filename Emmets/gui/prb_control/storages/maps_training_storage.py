# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/storages/maps_training_storage.py
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IMapsTrainingController

class MapsTrainingStorage(SessionStorage):
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)

    def isModeSelected(self):
        return super(MapsTrainingStorage, self).isModeSelected() and self.mapsTrainingController.isMapsTrainingEnabled

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isMapsTraining()