# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/constants/loot_box_bonus_group.py
from frameworks.wulf import ViewModel

class LootBoxBonusGroup(ViewModel):
    __slots__ = ()
    VEHICLE = 'vehicle'
    PREMIUM = 'premium'
    CURRENCY = 'currency'
    VEHICLECUSTOMIZATIONS = 'vehicleCustomizations'
    CREW = 'crew'
    BOOSTERS = 'boosters'
    EQUIPMENTS = 'equipments'
    ACCOUNTCUSTOMIZATIONS = 'accountCustomizations'
    FEATUREITEMS = 'featureItems'
    LOOTBOX_STAGE_ROTATION = 'lootboxStageRotation'

    def __init__(self, properties=0, commands=0):
        super(LootBoxBonusGroup, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LootBoxBonusGroup, self)._initialize()