# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/services_config.py
import logging, festivity
__all__ = ('getClientServicesConfig', )
_logger = logging.getLogger(__name__)

def getClientServicesConfig(manager):
    import account_helpers, connection_mgr, MapActivities, dyn_objects_cache, gui, gameplay, helpers, uilogging
    from vehicle_systems.appearance_cache import AppearanceCache
    from skeletons.connection_mgr import IConnectionManager
    from skeletons.map_activities import IMapActivities
    from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
    from skeletons.vehicle_appearance_cache import IAppearanceCache
    manager.addInstance(IConnectionManager, connection_mgr.ConnectionManager(), finalizer='fini')
    manager.addInstance(IMapActivities, MapActivities.MapActivities(), finalizer='destroy')
    manager.addInstance(IBattleDynamicObjectsCache, dyn_objects_cache.BattleDynamicObjectsCache(), finalizer='destroy')
    manager.addInstance(IAppearanceCache, AppearanceCache(), finalizer='clear')
    manager.addConfig(account_helpers.getAccountHelpersConfig)
    manager.addConfig(gameplay.getGameplayConfig)
    manager.addConfig(festivity.getFestivityConfig)
    manager.addConfig(gui.getGuiServicesConfig)
    manager.addConfig(uilogging.getUILoggingConfig)
    manager.addConfig(helpers.getHelperServicesConfig)
    import constants
    from gui import GUI_SETTINGS
    if constants.IS_TUTORIAL_ENABLED and GUI_SETTINGS.isGuiEnabled():
        try:
            import tutorial
        except ImportError:
            _logger.exception('Module tutorial not found')
            from helpers import tutorial

    else:
        from helpers import tutorial
    manager.addConfig(tutorial.getTutorialConfig)