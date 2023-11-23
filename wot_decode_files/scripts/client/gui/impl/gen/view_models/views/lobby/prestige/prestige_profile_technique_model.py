# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_profile_technique_model.py
from gui.impl.gen.view_models.views.lobby.prestige.prestige_base_model import PrestigeBaseModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class PrestigeProfileTechniqueModel(PrestigeBaseModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PrestigeProfileTechniqueModel, self).__init__(properties=properties, commands=commands)

    @property
    def nextEmblem(self):
        return self._getViewModel(3)

    @staticmethod
    def getNextEmblemType():
        return PrestigeEmblemModel

    def _initialize(self):
        super(PrestigeProfileTechniqueModel, self)._initialize()
        self._addViewModelProperty('nextEmblem', PrestigeEmblemModel())