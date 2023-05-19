# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_view_adaptor.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.veh_post_progression.post_progression_cfg_component import PostProgressionCfgComponentView
from gui.impl.lobby.veh_post_progression.post_progression_cmp_component import PostProgressionCmpComponentView

class VehiclePostProgressionViewAdaptor(InjectComponentAdaptor):
    __slots__ = ('__ctx', )

    def __init__(self, ctx):
        super(VehiclePostProgressionViewAdaptor, self).__init__()
        self.__ctx = ctx

    def _makeInjectView(self):
        parentAlias = self.__ctx['parentAlias']
        if parentAlias == VIEW_ALIAS.VEH_POST_PROGRESSION:
            return PostProgressionCfgComponentView(**self.__ctx)
        if parentAlias == VIEW_ALIAS.VEH_POST_PROGRESSION_CMP:
            return PostProgressionCmpComponentView(**self.__ctx)