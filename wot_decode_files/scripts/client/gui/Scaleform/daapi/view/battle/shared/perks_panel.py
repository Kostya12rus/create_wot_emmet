# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/perks_panel.py
from gui.Scaleform.daapi.view.meta.PerksPanelMeta import PerksPanelMeta
import WWISE, BigWorld
from items import tankmen
from shared_utils import CONST_CONTAINER
from helpers import dependency
from items.components.perks_constants import PerkState
from skeletons.gui.battle_session import IBattleSessionProvider

class PerksSounds(CONST_CONTAINER):
    PERK = 'detachment_perk'


class PerksPanel(PerksPanelMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def setPerks(self, perks):
        self.clearHUD()
        perksData = []
        for perkData in sorted(perks, key=(lambda k: k['perkID'])):
            perkID = perkData['perkID']
            skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
            perk = {'perkName': skillName, 
               'state': perkData['state'], 
               'duration': perkData['coolDown'], 
               'lifeTime': self._getLifeTime(perkData)}
            perksData.append(perk)

        self.as_setPerksS(perksData)

    def updatePerks(self, changedPerks, prevPerks):
        for perkID, perkData in changedPerks.iteritems():
            lifeTime = self._getLifeTime(perkData)
            state = perkData['state']
            skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
            self.as_updatePerkS(skillName, state, perkData['coolDown'], lifeTime)
            if state == PerkState.ACTIVE:
                if perkID not in prevPerks or prevPerks[perkID]['state'] != PerkState.ACTIVE:
                    WWISE.WW_eventGlobal(PerksSounds.PERK)

    def clearHUD(self):
        self.as_clearPanelS()

    def _getLifeTime(self, perkData):
        lifeTimeServer = perkData['lifeTime']
        if BigWorld.serverTime() < lifeTimeServer:
            return lifeTimeServer - BigWorld.serverTime()
        return -1