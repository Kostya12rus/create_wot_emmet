# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/comp7/full_stats.py
from gui.Scaleform.daapi.view.battle.comp7.comp7_voip_helper import Comp7VoipHelper, VoiceChatControlTextStyles
from gui.Scaleform.daapi.view.meta.Comp7FullStatsMeta import Comp7FullStatsMeta

class FullStatsComponent(Comp7FullStatsMeta):

    def __init__(self):
        super(FullStatsComponent, self).__init__()
        self.__voipHelper = Comp7VoipHelper(component=self, textStyle=VoiceChatControlTextStyles.FULL_STATS)

    def onVoiceChatControlClick(self):
        self.__voipHelper.onVoiceChatControlClick()

    def _populate(self):
        super(FullStatsComponent, self)._populate()
        self.__voipHelper.populate()
        self.__voipHelper.enable(enable=True)

    def _dispose(self):
        self.__voipHelper.dispose()
        super(FullStatsComponent, self)._dispose()

    @staticmethod
    def _buildTabs(builder):
        builder.addStatisticsTab()
        builder.addBoostersTab()
        return builder.getTabs()