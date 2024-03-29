# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/blueprints/blueprints_alliance_tooltip_view.py
import nations
from frameworks.wulf import ViewSettings, Array
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.blueprints.blueprint_price import BlueprintPrice
from gui.impl.gen.view_models.views.lobby.blueprints.blueprints_alliance_tooltip_view_model import BlueprintsAllianceTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class BlueprintsAllianceTooltipView(ViewImpl):
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, nation, vehicleIntCD, vehicleLevel):
        self.__nation = nation
        self.__vehicleIntCD = vehicleIntCD
        self.__vehicleLevel = vehicleLevel
        settings = ViewSettings(layoutID=R.views.lobby.blueprints.tooltips.BlueprintsAlliancesTooltipView(), model=BlueprintsAllianceTooltipViewModel())
        super(BlueprintsAllianceTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BlueprintsAllianceTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        nationId = nations.INDICES[self.__nation]
        allianceId = nations.NATION_TO_ALLIANCE_IDS_MAP[nationId]
        with self.viewModel.transaction() as (model):
            model.setAllianceName(nations.ALLIANCES_TAGS_ORDER[allianceId])
            model.setVehicleNationName(self.__nation)
            self.__setPriceOptions(model.getPriceOptions())

    def __setPriceOptions(self, arrayModel):
        arrayModel.clear()
        options = self.__itemsCache.items.blueprints.getNationalRequiredOptions(self.__vehicleIntCD, self.__vehicleLevel)
        for nId, cost in options.iteritems():
            price = BlueprintPrice()
            price.setNationName(nations.MAP[nId])
            price.setValue(int(cost))
            arrayModel.addViewModel(price)

        arrayModel.invalidate()