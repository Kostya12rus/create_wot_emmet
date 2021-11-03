# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/settings_core/__init__.py
from skeletons.account_helpers.settings_core import ISettingsCache, ISettingsCore

def getSettingsCoreConfig(manager):
    from account_helpers.settings_core.SettingsCache import SettingsCache
    from account_helpers.settings_core.SettingsCore import SettingsCore
    cache = SettingsCache()
    manager.addInstance(ISettingsCache, cache, finalizer='fini')
    core = SettingsCore()
    manager.addInstance(ISettingsCore, core, finalizer='fini')
    cache.init()
    core.init()