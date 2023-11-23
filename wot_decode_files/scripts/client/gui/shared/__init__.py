# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/__init__.py
from gui.shared.event_bus import EventBus, EVENT_BUS_SCOPE, EventPriority
__all__ = ('g_eventBus', 'getSharedServices', 'EVENT_BUS_SCOPE', 'EventPriority')
g_eventBus = EventBus()

def getSharedServices(manager):
    from gui.turret_gun_angles import TurretAndGunAngles
    from gui.shared.items_cache import ItemsCache
    from gui.shared.gui_items.factories import GuiItemFactory
    from gui.shared.utils.HangarSpace import HangarSpace
    from gui.shared.utils.hangar_space_reloader import HangarSpaceReloader
    from gui.shared.utils.RareAchievementsCache import RaresCache
    from skeletons.gui.turret_gun_angles import ITurretAndGunAngles
    from skeletons.gui.shared import IItemsCache
    from skeletons.gui.shared.gui_items import IGuiItemsFactory
    from skeletons.gui.shared.utils import IHangarSpace
    from skeletons.gui.shared.utils import IHangarSpaceReloader
    from skeletons.gui.shared.utils import IRaresCache
    cache = ItemsCache()
    cache.init()
    manager.addInstance(IItemsCache, cache, finalizer='fini')
    itemsFactory = GuiItemFactory()
    manager.addInstance(IGuiItemsFactory, itemsFactory)
    manager.addInstance(ITurretAndGunAngles, TurretAndGunAngles())
    manager.addRuntime(IHangarSpace, HangarSpace)
    hangarSpaceReloader = HangarSpaceReloader()
    hangarSpaceReloader.init()
    manager.addInstance(IHangarSpaceReloader, hangarSpaceReloader, finalizer='destroy')
    manager.addInstance(IRaresCache, RaresCache())