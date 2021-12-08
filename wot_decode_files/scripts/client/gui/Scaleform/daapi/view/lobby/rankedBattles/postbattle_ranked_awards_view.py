# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/postbattle_ranked_awards_view.py
import SoundGroups
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_OVERLAY_SOUND_SPACE
from gui.ranked_battles.ranked_builders.postbattle_awards_vos import getVOsSequence
from gui.Scaleform.daapi.view.meta.RankedBattlesAwardsViewMeta import RankedBattlesAwardsViewMeta
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class PostbattleRankedAwardsView(RankedBattlesAwardsViewMeta):
    _COMMON_SOUND_SPACE = RANKED_OVERLAY_SOUND_SPACE
    __rankedController = dependency.descriptor(IRankedBattlesController)
    __slots__ = ('__awardsSequence', '__rankedInfo')

    def __init__(self, ctx=None):
        super(PostbattleRankedAwardsView, self).__init__()
        self.__awardsSequence = ctx['awardsSequence']
        self.__rankedInfo = ctx['rankedInfo']

    def closeView(self):
        self.__close()

    def onSoundTrigger(self, triggerName):
        SoundGroups.g_instance.playSound2D(triggerName)

    def _populate(self):
        super(PostbattleRankedAwardsView, self)._populate()
        vosSequence = getVOsSequence(self.__awardsSequence, self.__rankedController.getRanksChain(min(self.__awardsSequence, key=lambda x: x.rankID).rankID if self.__awardsSequence else 0, max(self.__awardsSequence, key=lambda x: x.rankID).rankID + 1 if self.__awardsSequence else 0), self.__rankedInfo)
        self.as_setDataS({'vosSequence': vosSequence, 
           'title': backport.text(R.strings.ranked_battles.awards.congratulation()), 
           'nextButtonLabel': backport.text(R.strings.ranked_battles.awards.yes())})

    def _dispose(self):
        self.onSoundTrigger(RANKEDBATTLES_ALIASES.SOUND_AWARD_QUALIFICATION_STOP)
        super(PostbattleRankedAwardsView, self)._dispose()

    def __close(self):
        self.destroy()