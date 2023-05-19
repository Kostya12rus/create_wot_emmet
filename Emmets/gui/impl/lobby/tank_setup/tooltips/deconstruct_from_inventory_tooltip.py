# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/tooltips/deconstruct_from_inventory_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.deconstruct_from_inventory_tooltip_model import DeconstructFromInventoryTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class DeconstructFromInventoryTooltip(ViewImpl):
    __slots__ = ('equipmentName', 'equipmentAmount')

    def __init__(self, equipmentName, equipmentAmount, layoutID=R.views.lobby.tanksetup.tooltips.DeconstructFromInventoryTooltip()):
        settings = ViewSettings(layoutID)
        settings.model = DeconstructFromInventoryTooltipModel()
        self.equipmentName = equipmentName
        self.equipmentAmount = equipmentAmount
        super(DeconstructFromInventoryTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(DeconstructFromInventoryTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(DeconstructFromInventoryTooltip, self)._initialize(*args, **kwargs)
        self.viewModel.setEquipmentAmount(self.equipmentAmount)
        self.viewModel.setEquipmentName(self.equipmentName)