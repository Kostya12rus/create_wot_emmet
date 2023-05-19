# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_dialog_slot_model.py
from gui.impl.gen.view_models.views.lobby.premacc.maps_blacklist_slot_model import MapsBlacklistSlotModel

class MapsBlacklistDialogSlotModel(MapsBlacklistSlotModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MapsBlacklistDialogSlotModel, self).__init__(properties=properties, commands=commands)

    def getIsResizable(self):
        return self._getBool(5)

    def setIsResizable(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(MapsBlacklistDialogSlotModel, self)._initialize()
        self._addBoolProperty('isResizable', False)