# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/__init__.py
from gui.Scaleform.framework.entities.View import View
from gui.shared.ny_vignette_settings_switcher import checkVignetteSettings

class LobbySubView(View):
    __background_alpha__ = 0.6

    def setEnvironment(self, app):
        checkVignetteSettings(self.uniqueName)
        app.setBackgroundAlpha(self.__background_alpha__)
        super(LobbySubView, self).setEnvironment(app)