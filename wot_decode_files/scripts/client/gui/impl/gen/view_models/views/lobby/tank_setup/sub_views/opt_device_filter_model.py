# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/opt_device_filter_model.py
from gui.impl.gen.view_models.views.lobby.tank_setup.common.filters_model import FiltersModel

class OptDeviceFilterModel(FiltersModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=2):
        super(OptDeviceFilterModel, self).__init__(properties=properties, commands=commands)

    def getSelectedCount(self):
        return self._getNumber(4)

    def setSelectedCount(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(OptDeviceFilterModel, self)._initialize()
        self._addNumberProperty('selectedCount', 0)