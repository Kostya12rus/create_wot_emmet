# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/account_settings_helper.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR
from helpers import dependency
from shared_utils import CONST_CONTAINER
from skeletons.account_helpers.settings_core import ISettingsCore

class WelcomeScreen(CONST_CONTAINER):
    CREW_22_WELCOME = 'crew22Welcome'


class AccountSettingsHelper(object):
    settingsCore = dependency.descriptor(ISettingsCore)

    @classmethod
    def welcomeScreenShown(cls, screen):
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        settings = cls.settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)
        settings[screen] = True
        cls.settingsCore.serverSettings.setSectionSettings(GUI_START_BEHAVIOR, settings)

    @classmethod
    def isWelcomeScreenShown(cls, screen):
        settingsCore = dependency.instance(ISettingsCore)
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        settings = settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)
        return settings.get(screen, False)