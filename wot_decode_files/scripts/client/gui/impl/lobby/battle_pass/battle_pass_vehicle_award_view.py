# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/battle_pass_vehicle_award_view.py
import SoundGroups
from frameworks.wulf import ViewSettings
from gui.battle_pass.sounds import BattlePassSounds
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_vehicle_award_view_model import BattlePassVehicleAwardViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.sounds.filters import switchHangarOverlaySoundFilter
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class BattlePassVehicleAwardView(ViewImpl):
    __slots__ = ()
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, layoutID, *args, **kwargs):
        settings = ViewSettings(layoutID)
        settings.model = BattlePassVehicleAwardViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(BattlePassVehicleAwardView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattlePassVehicleAwardView, self).getViewModel()

    def _initialize(self, data, *args, **kwargs):
        super(BattlePassVehicleAwardView, self)._initialize(*args, **kwargs)
        self.viewModel.setVehicleLevelPoints(data.get('vehiclePoints', 0))
        self.viewModel.setBattlePassPointsAward(data.get('bonusPoints', 0))
        vehicle = self.__itemsCache.items.getItemByCD(data.get('vehTypeCompDescr', 0))
        self.viewModel.setIsPremiumVehicle(vehicle.isPremium)
        self.viewModel.setIsEliteVehicle(vehicle.isElite)
        self.viewModel.setVehicleLevel(vehicle.level)
        self.viewModel.setVehicleName(vehicle.userName)
        self.viewModel.setVehicleNation(vehicle.nationName)
        self.viewModel.setVehicleType(vehicle.type)
        techName = vehicle.name.split(':')
        self.viewModel.setTechName(techName[1])
        switchHangarOverlaySoundFilter(on=True)
        SoundGroups.g_instance.playSound2D(BattlePassSounds.TANK_POINTS_CAP)

    def _finalize(self):
        super(BattlePassVehicleAwardView, self)._finalize()
        switchHangarOverlaySoundFilter(on=False)


class BattlePassVehicleAwardWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, data):
        super(BattlePassVehicleAwardWindow, self).__init__(content=BattlePassVehicleAwardView(R.views.lobby.battle_pass.BattlePassVehicleAwardView(), data=data))