# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/common/ammunition_panel/ammunition_blocks_controller.py
import typing
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_shells_section import AmmunitionShellsSection
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.common.tabs_controller import TabsController, tabUpdateFunc
from gui.impl.common.ammunition_panel.ammunition_panel_blocks import OptDeviceBlock, ShellsBlock, ConsumablesBlock, BattleBoostersBlock, BattleAbilitiesBlock
if typing.TYPE_CHECKING:
    from gui.impl.common.ammunition_panel.ammunition_groups_controller import GroupData

class BaseAmmunitionBlocksController(TabsController):
    __slots__ = ('_vehicle', '_currentSection', '_sections', '_ctx')

    def __init__(self, vehicle, autoCreating=True, ctx=None):
        super(BaseAmmunitionBlocksController, self).__init__(autoCreating)
        self._vehicle = vehicle
        self._currentSection = None
        self._ctx = ctx
        self._sections = {}
        return

    def updateVehicle(self, vehicle):
        self._vehicle = vehicle

    def updateCurrentSection(self, currentSection):
        self._currentSection = currentSection

    def getSectionsByGroup(self, groupID):
        return self._sections.get(groupID, ())

    def addSections(self, group):
        self._sections.update({group.groupID: group.sections})

    def _getTabs(self, **kwargs):
        if self._vehicle is None:
            return []
        else:
            groupID = kwargs.get('groupID', None)
            return self._sections.get(groupID, [])


class AmmunitionBlocksController(BaseAmmunitionBlocksController):
    __slots__ = ()

    @tabUpdateFunc(TankSetupConstants.OPT_DEVICES)
    def _updateOptDevices(self, viewModel, isFirst=False):
        OptDeviceBlock(self._vehicle, self._currentSection, ctx=self._ctx).adapt(viewModel, isFirst)

    @tabUpdateFunc(TankSetupConstants.SHELLS)
    def _updateShells(self, viewModel, isFirst=False):
        ShellsBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)

    @tabUpdateFunc(TankSetupConstants.CONSUMABLES)
    def _updateConsumables(self, viewModel, isFirst=False):
        ConsumablesBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)

    @tabUpdateFunc(TankSetupConstants.BATTLE_BOOSTERS)
    def _updateBattleBoosters(self, viewModel, isFirst=False):
        BattleBoostersBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)

    @tabUpdateFunc(TankSetupConstants.BATTLE_ABILITIES)
    def _updateBattleAbilities(self, viewModel, isFirst=False):
        BattleAbilitiesBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)

    def _createViewModel(self, name):
        if name == TankSetupConstants.SHELLS:
            return AmmunitionShellsSection()
        return AmmunitionItemsSection()