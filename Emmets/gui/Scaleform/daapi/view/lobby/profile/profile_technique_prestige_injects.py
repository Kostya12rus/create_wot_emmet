# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/profile_technique_prestige_injects.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.prestige.prestige_profile_technique_views import PrestigeProfileTechniqueView, PrestigeProfileTechniqueEmblemView
from gui.prb_control.entities.listener import IGlobalListener

class CommonPrestigeInject(InjectComponentAdaptor, IGlobalListener):

    def setDatabaseID(self, value):
        self._injectView.setDatabaseID(value)

    def setSelectedVehicleIntCD(self, value):
        self._injectView.setSelectedVehicleIntCD(value)

    def _makeInjectView(self):
        raise NotImplementedError


class ProfileTechniquePrestigeInject(CommonPrestigeInject):

    def _makeInjectView(self):
        return PrestigeProfileTechniqueView()


class ProfileTechniquePrestigeEmblemInject(CommonPrestigeInject):

    def _makeInjectView(self):
        return PrestigeProfileTechniqueEmblemView()