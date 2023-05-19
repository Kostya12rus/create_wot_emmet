# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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