# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/settings_core/settings_disable/aop.py
from helpers import aop
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Dict, Sequence

class _FlashDisableSettingsAspect(aop.Aspect):

    def __init__(self, settings):
        super(_FlashDisableSettingsAspect, self).__init__()
        self.__disabledSettings = settings

    def atCall(self, cd):
        for itemId, guiPath in self.__disabledSettings.iteritems():
            self.__disableControl(cd, itemId, guiPath)

    def __disableControl(self, cd, itemId, guiPath):
        page = ''
        subpage = ''
        pathLen = len(guiPath)
        if pathLen == 1:
            page = guiPath[0]
        elif pathLen == 2:
            page, subpage = guiPath
        cd.self.as_disableControlS(page, itemId, subpage)


class DisableCameraSettingsFlashPointcut(aop.Pointcut):

    def __init__(self, settings):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.common.settings.SettingsWindow', 'SettingsWindow', 'as_setDataS')
        self.addAspect(_FlashDisableSettingsAspect, settings=settings)


class DisableAltModeTogglePointcut(aop.Pointcut):

    def __init__(self):
        super(DisableAltModeTogglePointcut, self).__init__('AvatarInputHandler.control_modes', 'ArcadeControlMode', '^__activateAlternateMode$')