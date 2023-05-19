# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/crew_xp_panel_inject.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.crew.crew_header_view import CrewHeaderView
from gui.Scaleform.daapi.view.meta.CrewXPPanelInjectMeta import CrewXPPanelInjectMeta
from gui.prb_control.entities.listener import IGlobalListener

class CrewXPPanelInject(InjectComponentAdaptor, CrewXPPanelInjectMeta, IGlobalListener):

    def _makeInjectView(self):
        return CrewHeaderView()