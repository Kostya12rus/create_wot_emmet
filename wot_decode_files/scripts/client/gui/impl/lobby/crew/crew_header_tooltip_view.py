# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/crew_header_tooltip_view.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_header_tooltip_view_model import CrewHeaderTooltipViewModel
from gui.impl.gen.view_models.views.lobby.crew.idle_crew_bonus import IdleCrewBonusEnum
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle
_MINUTES_MULTIPLICATOR = 5

class CrewHeaderTooltipView(ViewImpl):
    __slots__ = ('_serverSettings', )
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(layoutID=R.views.lobby.crew.CrewHeaderTooltipView(), model=CrewHeaderTooltipViewModel())
        settings.args = args
        settings.kwargs = kwargs
        self._serverSettings = self._lobbyContext.getServerSettings()
        super(CrewHeaderTooltipView, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return super(CrewHeaderTooltipView, self).getViewModel()

    def _onLoading(self, idleCrewBonus):
        with self.viewModel.transaction() as (tx):
            tx.setBonusXpPerFiveMinutes(self._serverSettings.getRenewableSubCrewXPPerMinute() * _MINUTES_MULTIPLICATOR)
            tx.setIdleCrewBonus(idleCrewBonus)
            vehicle = self._itemsCache.items.getVehicle(self._wotPlusCtrl.getVehicleIDWithIdleXP())
            if vehicle:
                tx.setVehicleName(vehicle.userName)
                tx.setVehicleType(vehicle.typeUserName)
                tx.setVehicleLvl(str(vehicle.level))