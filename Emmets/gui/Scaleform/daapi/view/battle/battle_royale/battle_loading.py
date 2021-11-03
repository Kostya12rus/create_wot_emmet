# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/battle_royale/battle_loading.py
from gui.Scaleform.daapi.view.meta.BattleRoyaleLoadingMeta import BattleRoyaleLoadingMeta
from gui.impl.gen.resources import R
from gui.impl import backport

class BattleLoading(BattleRoyaleLoadingMeta):

    def _populate(self):
        super(BattleLoading, self)._populate()
        arenaDP = self.sessionProvider.getArenaDP()
        self.as_setHeaderDataS({'battleType': arenaDP.getPersonalDescription().getFrameLabel(), 
           'title': backport.text(R.strings.battle_royale.fullStats.title()), 
           'subTitle': backport.text(R.strings.battle_royale.fullStats.subTitle()), 
           'description': backport.text(R.strings.battle_royale.fullStats.description())})

    def _formatTipTitle(self, tipTitleText):
        return tipTitleText

    def _formatTipBody(self, tipBody):
        return tipBody

    def _makeVisualTipVO(self, arenaDP, tip=None):
        vo = {'tipIcon': self.gui.resourceManager.getImagePath(tip.icon) if tip is not None else None}
        return vo