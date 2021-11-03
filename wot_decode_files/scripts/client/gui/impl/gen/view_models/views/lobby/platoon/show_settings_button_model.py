# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/show_settings_button_model.py
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class ShowSettingsButtonModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=1):
        super(ShowSettingsButtonModel, self).__init__(properties=properties, commands=commands)

    def getIsPressed(self):
        return self._getBool(4)

    def setIsPressed(self, value):
        self._setBool(4, value)

    def getHasPopover(self):
        return self._getBool(5)

    def setHasPopover(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(ShowSettingsButtonModel, self)._initialize()
        self._addBoolProperty('isPressed', False)
        self._addBoolProperty('hasPopover', False)