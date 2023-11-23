# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/classic/map_info_tip.py
from gui.Scaleform.daapi.view.meta.MapInfoTipMeta import MapInfoTipMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class MapInfoTip(MapInfoTipMeta):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _populate(self):
        super(MapInfoTip, self)._populate()
        self.as_setEnabledS(self.__sessionProvider.arenaVisitor.extra.isMapsInDevelopmentEnabled())