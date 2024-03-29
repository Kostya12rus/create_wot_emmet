# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_balance_content_model.py
from gui.impl.gen.view_models.views.common_balance_content_model import CommonBalanceContentModel
from gui.impl.gen.view_models.views.lobby.blueprints.fragment_item_model import FragmentItemModel

class BlueprintBalanceContentModel(CommonBalanceContentModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BlueprintBalanceContentModel, self).__init__(properties=properties, commands=commands)

    @property
    def intelligenceBalance(self):
        return self._getViewModel(1)

    @staticmethod
    def getIntelligenceBalanceType():
        return FragmentItemModel

    def getAllianceName(self):
        return self._getString(2)

    def setAllianceName(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(BlueprintBalanceContentModel, self)._initialize()
        self._addViewModelProperty('intelligenceBalance', FragmentItemModel())
        self._addStringProperty('allianceName', '')