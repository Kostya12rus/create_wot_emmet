# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_widget_3d_style_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class BattlePassWidget3DStyleViewModel(ViewModel):
    __slots__ = ('onPreviewClick', 'onExtraPreviewClick')

    def __init__(self, properties=3, commands=2):
        super(BattlePassWidget3DStyleViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getStyleName(self):
        return self._getString(1)

    def setStyleName(self, value):
        self._setString(1, value)

    def getStyleId(self):
        return self._getNumber(2)

    def setStyleId(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(BattlePassWidget3DStyleViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addStringProperty('styleName', '')
        self._addNumberProperty('styleId', 0)
        self.onPreviewClick = self._addCommand('onPreviewClick')
        self.onExtraPreviewClick = self._addCommand('onExtraPreviewClick')