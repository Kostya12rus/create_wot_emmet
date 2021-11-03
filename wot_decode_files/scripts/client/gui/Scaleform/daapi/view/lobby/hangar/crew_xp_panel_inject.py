# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/crew_xp_panel_inject.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.crew.crew_header_view import CrewHeaderView
from gui.Scaleform.daapi.view.meta.CrewXPPanelInjectMeta import CrewXPPanelInjectMeta
from gui.prb_control.entities.listener import IGlobalListener

class CrewXPPanelInject(InjectComponentAdaptor, CrewXPPanelInjectMeta, IGlobalListener):

    def _makeInjectView(self):
        return CrewHeaderView()