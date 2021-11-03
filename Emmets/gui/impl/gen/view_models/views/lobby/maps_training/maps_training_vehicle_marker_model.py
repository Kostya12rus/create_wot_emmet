# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/maps_training/maps_training_vehicle_marker_model.py
from frameworks.wulf import ViewModel

class MapsTrainingVehicleMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(MapsTrainingVehicleMarkerModel, self).__init__(properties=properties, commands=commands)

    def getTop(self):
        return self._getReal(0)

    def setTop(self, value):
        self._setReal(0, value)

    def _initialize(self):
        super(MapsTrainingVehicleMarkerModel, self)._initialize()
        self._addRealProperty('top', 0.0)