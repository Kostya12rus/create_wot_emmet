# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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