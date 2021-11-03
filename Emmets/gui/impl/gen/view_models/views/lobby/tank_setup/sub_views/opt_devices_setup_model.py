# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/opt_devices_setup_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_filter_model import OptDeviceFilterModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.opt_device_slot_model import OptDeviceSlotModel

class OptDevicesSetupModel(BaseSetupModel):
    __slots__ = ('onIntroPassed', )

    def __init__(self, properties=9, commands=8):
        super(OptDevicesSetupModel, self).__init__(properties=properties, commands=commands)

    @property
    def filter(self):
        return self._getViewModel(5)

    def getSlots(self):
        return self._getArray(6)

    def setSlots(self, value):
        self._setArray(6, value)

    def getWithIntroduction(self):
        return self._getBool(7)

    def setWithIntroduction(self, value):
        self._setBool(7, value)

    def getIntroductionType(self):
        return self._getString(8)

    def setIntroductionType(self, value):
        self._setString(8, value)

    def _initialize(self):
        super(OptDevicesSetupModel, self)._initialize()
        self._addViewModelProperty('filter', OptDeviceFilterModel())
        self._addArrayProperty('slots', Array())
        self._addBoolProperty('withIntroduction', False)
        self._addStringProperty('introductionType', '')
        self.onIntroPassed = self._addCommand('onIntroPassed')