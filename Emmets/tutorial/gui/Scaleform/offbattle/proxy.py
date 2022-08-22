# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/offbattle/proxy.py
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player
from tutorial.gui.Scaleform.lobby import SfLobbyProxy
from tutorial.gui.Scaleform.offbattle import settings

class SfOffbattleProxy(SfLobbyProxy):

    def __init__(self):
        effects = {GUI_EFFECT_NAME.SHOW_DIALOG: effects_player.ShowDialogEffect(settings.DIALOG_ALIAS_MAP), 
           GUI_EFFECT_NAME.SHOW_WINDOW: effects_player.ShowWindowEffect(settings.WINDOW_ALIAS_MAP), 
           GUI_EFFECT_NAME.UPDATE_CONTENT: effects_player.UpdateContentEffect()}
        super(SfOffbattleProxy, self).__init__(effects_player.EffectsPlayer(effects))

    def getViewSettings(self):
        return settings.OFFBATTLE_VIEW_SETTINGS