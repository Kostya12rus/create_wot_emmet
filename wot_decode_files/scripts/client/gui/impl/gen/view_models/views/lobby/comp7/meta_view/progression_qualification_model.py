# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/comp7/meta_view/progression_qualification_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.qualification_battle import QualificationBattle
from gui.impl.gen.view_models.views.lobby.comp7.qualification_model import QualificationModel

class ProgressionQualificationModel(QualificationModel):
    __slots__ = ('onRankRewardsPageOpen', )

    def __init__(self, properties=5, commands=1):
        super(ProgressionQualificationModel, self).__init__(properties=properties, commands=commands)

    def getBattles(self):
        return self._getArray(4)

    def setBattles(self, value):
        self._setArray(4, value)

    @staticmethod
    def getBattlesType():
        return QualificationBattle

    def _initialize(self):
        super(ProgressionQualificationModel, self)._initialize()
        self._addArrayProperty('battles', Array())
        self.onRankRewardsPageOpen = self._addCommand('onRankRewardsPageOpen')