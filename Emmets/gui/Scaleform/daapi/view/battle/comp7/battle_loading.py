# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/battle_loading.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from account_helpers.settings_core.options import BattleLoadingTipSetting

class Comp7BattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        result = super(Comp7BattleLoading, self)._getViewSettingByID(settingID)
        result.update({'leftTeamTitleLeft': -483, 
           'rightTeamTitleLeft': 275})
        return result

    def _makeVisualTipVO(self, arenaDP, tip=None):
        settingID = BattleLoadingTipSetting.OPTIONS.MINIMAP
        vo = {'settingID': settingID, 
           'tipIcon': None, 
           'arenaTypeID': self._arenaVisitor.type.getID(), 
           'minimapTeam': arenaDP.getNumberOfTeam(), 
           'showMinimap': True, 
           'showTipsBackground': True}
        vo.update(self._getViewSettingByID(settingID))
        return vo