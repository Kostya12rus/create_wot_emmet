# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/chains/proxy.py
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player
from tutorial.gui.Scaleform.chains import settings
from tutorial.gui.Scaleform.lobby.proxy import SfLobbyProxy

class SfChainsProxy(SfLobbyProxy):

    def __init__(self):
        effects = {GUI_EFFECT_NAME.SHOW_HINT: effects_player.ShowChainHint(), 
           GUI_EFFECT_NAME.SHOW_WINDOW: effects_player.ShowWindowEffect(settings.WINDOW_ALIAS_MAP), 
           GUI_EFFECT_NAME.SET_CRITERIA: effects_player.SetCriteriaEffect(), 
           GUI_EFFECT_NAME.SET_TRIGGER: effects_player.SetTriggerEffect()}
        super(SfChainsProxy, self).__init__(effects_player.EffectsPlayer(effects))

    def getViewSettings(self):
        return settings.CHAINS_VIEW_SETTINGS

    def getViewsAliases(self):
        return settings.WINDOW_ALIAS_MAP