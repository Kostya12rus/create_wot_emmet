# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/button_find_players_cancel_search_model.py
from gui.impl.gen.view_models.views.lobby.platoon.custom_sound_button_model import CustomSoundButtonModel

class ButtonFindPlayersCancelSearchModel(CustomSoundButtonModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(ButtonFindPlayersCancelSearchModel, self).__init__(properties=properties, commands=commands)

    def getIsLight(self):
        return self._getBool(7)

    def setIsLight(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(ButtonFindPlayersCancelSearchModel, self)._initialize()
        self._addBoolProperty('isLight', True)