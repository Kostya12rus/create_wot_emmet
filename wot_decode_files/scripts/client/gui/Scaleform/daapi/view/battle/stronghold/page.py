# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/stronghold/page.py
from gui.Scaleform.daapi.view.battle.classic import ClassicPage
from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer
from gui.Scaleform.daapi.view.battle.stronghold.manager import StrongholdMarkersManager
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
_STRONGHOLD_EXTERNAL_COMPONENTS = (
 CrosshairPanelContainer, StrongholdMarkersManager)

class StrongholdPage(ClassicPage):

    def __init__(self, components=None, external=_STRONGHOLD_EXTERNAL_COMPONENTS, fullStatsAlias=BATTLE_VIEW_ALIASES.FULL_STATS):
        super(StrongholdPage, self).__init__(components=components, external=external, fullStatsAlias=fullStatsAlias)
        self.__soundControl = None
        return