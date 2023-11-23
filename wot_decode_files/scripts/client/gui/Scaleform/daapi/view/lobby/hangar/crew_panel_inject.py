# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/crew_panel_inject.py
from gui.Scaleform.daapi.view.meta.CrewPanelInjectMeta import CrewPanelInjectMeta
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.prb_control.entities.listener import IGlobalListener

class CrewPanelInject(InjectComponentAdaptor, CrewPanelInjectMeta, IGlobalListener):

    def _makeInjectView(self):
        from gui.impl.lobby.crew.hangar_crew_widget import HangarCrewWidget
        return HangarCrewWidget()

    def updateTankmen(self):
        self._injectView.updateTankmen()