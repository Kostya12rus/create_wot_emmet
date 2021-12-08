# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_congrats_types.py
from frameworks.wulf import ViewModel

class LootCongratsTypes(ViewModel):
    __slots__ = ()
    CONGRAT_TYPE_BLUEPRINT = 'BlueprintFinalFragmentCongrats'
    CONGRAT_TYPE_BLUEPRINT_PART = 'BlueprintVehicleFragmentCongrats'
    CONGRAT_TYPE_VEHICLE = 'VehicleLootBoxCongrats'
    CONGRAT_TYPE_STYLE = 'StyleLootBoxCongrats'
    CONGRAT_TYPE_TANKMAN = 'TankmanLootBoxCongrats'
    INIT_CONGRAT_TYPE_USUAL = 'UsualCongrats'
    INIT_CONGRAT_TYPE_PROGRESSIVE_REWARDS = 'ProgressiveRewardCongrats'
    INIT_CONGRAT_TYPE_CREW_BOOKS = 'CrewBookCongrats'
    INIT_CONGRAT_TYPE_LOOTBOX = 'LootBoxCongrats'
    INIT_CONGRAT_TYPE_EPIC_REWARDS = 'EpicRewardCongrats'
    INIT_CONGRAT_TYPE_BATTLE_PASS = 'BattlePassCongrats'
    INIT_CONGRAT_TYPE_AC_EMAIL_CONFIRMATION = 'ACEmailConfirmation'

    def __init__(self, properties=0, commands=0):
        super(LootCongratsTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LootCongratsTypes, self)._initialize()