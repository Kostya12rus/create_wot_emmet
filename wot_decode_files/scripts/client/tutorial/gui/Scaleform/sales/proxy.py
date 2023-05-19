# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/sales/proxy.py
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player
from tutorial.gui.Scaleform.lobby.proxy import SfLobbyProxy

class SfSalesProxy(SfLobbyProxy):

    def __init__(self):
        effects = {GUI_EFFECT_NAME.SHOW_HINT: effects_player.ShowChainHint(), 
           GUI_EFFECT_NAME.SET_CRITERIA: effects_player.SetCriteriaEffect(), 
           GUI_EFFECT_NAME.SET_TRIGGER: effects_player.SetTriggerEffect()}
        super(SfSalesProxy, self).__init__(effects_player.EffectsPlayer(effects))

    def getViewSettings(self):
        return {}

    def getViewsAliases(self):
        return {}