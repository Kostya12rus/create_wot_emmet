# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_royale/battle_result_view_model.py
from gui.impl.gen.view_models.views.battle_royale.battle_results.br_base_view_model import BrBaseViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.personal_results_model import PersonalResultsModel

class BattleResultViewModel(BrBaseViewModel):
    __slots__ = ('onHangarBtnClick', 'onCloseBtnClick')

    def __init__(self, properties=3, commands=2):
        super(BattleResultViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def personalResults(self):
        return self._getViewModel(2)

    @staticmethod
    def getPersonalResultsType():
        return PersonalResultsModel

    def _initialize(self):
        super(BattleResultViewModel, self)._initialize()
        self._addViewModelProperty('personalResults', PersonalResultsModel())
        self.onHangarBtnClick = self._addCommand('onHangarBtnClick')
        self.onCloseBtnClick = self._addCommand('onCloseBtnClick')