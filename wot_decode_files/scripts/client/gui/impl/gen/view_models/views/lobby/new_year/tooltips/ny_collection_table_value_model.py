# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/tooltips/ny_collection_table_value_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_single_collection_bonus_model import NySingleCollectionBonusModel

class NyCollectionTableValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(NyCollectionTableValueModel, self).__init__(properties=properties, commands=commands)

    @property
    def collectionBonuses(self):
        return self._getViewModel(0)

    def getInterval(self):
        return self._getString(1)

    def setInterval(self, value):
        self._setString(1, value)

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(NyCollectionTableValueModel, self)._initialize()
        self._addViewModelProperty('collectionBonuses', UserListModel())
        self._addStringProperty('interval', '1-10')
        self._addBoolProperty('isEnabled', False)