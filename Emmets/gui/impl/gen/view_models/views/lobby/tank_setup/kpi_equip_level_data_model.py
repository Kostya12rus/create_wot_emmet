# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/kpi_equip_level_data_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.main_content.kpi_item_model import KpiItemModel

class KpiEquipLevelDataModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(KpiEquipLevelDataModel, self).__init__(properties=properties, commands=commands)

    @property
    def value(self):
        return self._getViewModel(0)

    @staticmethod
    def getValueType():
        return KpiItemModel

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(KpiEquipLevelDataModel, self)._initialize()
        self._addViewModelProperty('value', KpiItemModel())
        self._addStringProperty('id', '')