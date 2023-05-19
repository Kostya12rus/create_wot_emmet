# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/mapbox/carousel_data_provider.py
from gui import GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_data_provider import BattlePassCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_helpers import getUnsuitable2queueTooltip
from gui.impl.gen import R
from gui.prb_control.entities.mapbox.pre_queue.actions_validator import MapboxVehicleValidator
from gui.shared.gui_items.Vehicle import Vehicle, VEHICLE_TYPES_ORDER_INDICES

class MapboxCarouselDataProvider(BattlePassCarouselDataProvider):

    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        return (
         cls._isSuitableForQueue(vehicle),
         not vehicle.isInInventory,
         not vehicle.isEvent,
         not vehicle.isOnlyForBattleRoyaleBattles,
         not vehicle.isFavorite,
         GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
         VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
         vehicle.level,
         tuple(vehicle.buyPrices.itemPrice.price.iterallitems(byWeight=True)),
         vehicle.userName)

    def _buildVehicle(self, vehicle):
        result = super(MapboxCarouselDataProvider, self)._buildVehicle(vehicle)
        state, _ = vehicle.getState()
        if state == Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE:
            validationResult = MapboxVehicleValidator.validateForMapbox(vehicle)
            resPath = R.strings.mapbox.mapboxCarousel.lockedTooltip
            if validationResult is not None:
                result['lockedTooltip'] = getUnsuitable2queueTooltip(validationResult, resPath)
        return result