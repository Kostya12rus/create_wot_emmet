# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_param_view_model.py
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import VehicleParamBaseViewModel

class VehicleParamViewModel(VehicleParamBaseViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(VehicleParamViewModel, self).__init__(properties=properties, commands=commands)

    def getLocalizedName(self):
        return self._getString(5)

    def setLocalizedName(self, value):
        self._setString(5, value)

    def getParentID(self):
        return self._getString(6)

    def setParentID(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(VehicleParamViewModel, self)._initialize()
        self._addStringProperty('localizedName', '')
        self._addStringProperty('parentID', '')