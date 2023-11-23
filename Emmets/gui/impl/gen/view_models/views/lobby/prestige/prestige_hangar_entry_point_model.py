# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_hangar_entry_point_model.py
from gui.impl.gen.view_models.views.lobby.prestige.prestige_base_model import PrestigeBaseModel

class PrestigeHangarEntryPointModel(PrestigeBaseModel):
    __slots__ = ('onShowInfo', )

    def __init__(self, properties=3, commands=1):
        super(PrestigeHangarEntryPointModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(PrestigeHangarEntryPointModel, self)._initialize()
        self.onShowInfo = self._addCommand('onShowInfo')