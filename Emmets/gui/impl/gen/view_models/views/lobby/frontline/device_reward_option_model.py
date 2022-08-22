# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/frontline/device_reward_option_model.py
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.kpi_description_model import KpiDescriptionModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_option_model import RewardOptionModel

class DeviceRewardOptionModel(RewardOptionModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(DeviceRewardOptionModel, self).__init__(properties=properties, commands=commands)

    @property
    def kpiDescriptions(self):
        return self._getViewModel(6)

    @staticmethod
    def getKpiDescriptionsType():
        return KpiDescriptionModel

    def getEffect(self):
        return self._getString(7)

    def setEffect(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(DeviceRewardOptionModel, self)._initialize()
        self._addViewModelProperty('kpiDescriptions', UserListModel())
        self._addStringProperty('effect', '')