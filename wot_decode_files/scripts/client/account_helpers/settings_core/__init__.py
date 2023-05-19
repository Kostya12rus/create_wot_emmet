# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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