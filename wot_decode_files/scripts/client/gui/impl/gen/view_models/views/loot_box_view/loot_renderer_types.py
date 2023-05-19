# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_view/loot_renderer_types.py
from frameworks.wulf import ViewModel

class LootRendererTypes(ViewModel):
    __slots__ = ()
    DEF = 'LootDefRenderer'
    VIDEO = 'LootVideoRenderer'
    VEHICLE = 'LootVehicleRenderer'
    VEHICLE_VIDEO = 'LootVehicleVideoRenderer'
    ANIMATED = 'LootAnimatedRenderer'
    CONVERSION = 'LootConversionRenderer'
    COMPENSATION = 'LootCompensationRenderer'
    CREWSKINS_COMPENSATION = 'CrewSkinsCompensationRenderer'
    VEHICLE_COMPENSATION = 'VehicleCompensationRenderer'
    VEHICLE_COMPENSATION_WITHOUT_ANIMATION = 'VehicleCompensationWithoutAnimationRenderer'
    BLUEPRINT_FINAL_FRAGMENT = 'BlueprintFinalFragmentRenderer'
    CREW_BOOK = 'CrewBookRenderer'

    def __init__(self, properties=0, commands=0):
        super(LootRendererTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LootRendererTypes, self)._initialize()