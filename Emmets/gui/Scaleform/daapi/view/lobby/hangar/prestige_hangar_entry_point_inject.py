# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/prestige_hangar_entry_point_inject.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.prestige.prestige_hangar_entry_point_view import PrestigeHangarEntryPointView
from gui.Scaleform.daapi.view.meta.PrestigeProgressInjectMeta import PrestigeProgressInjectMeta
from gui.prb_control.entities.listener import IGlobalListener
from shared_utils import nextTick

class PrestigeHangarEntryPointInject(InjectComponentAdaptor, PrestigeProgressInjectMeta, IGlobalListener):

    @nextTick
    def _createInjectView(self, *args):
        super(PrestigeHangarEntryPointInject, self)._createInjectView(*args)

    def _makeInjectView(self):
        return PrestigeHangarEntryPointView()