# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/popovers/random_battle_popover_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.mode_selector.popovers.random_battle_popover_item_model import RandomBattlePopoverItemModel

class RandomBattlePopoverModel(ViewModel):
    __slots__ = ('onItemChanged', )

    def __init__(self, properties=1, commands=1):
        super(RandomBattlePopoverModel, self).__init__(properties=properties, commands=commands)

    def getSettingsList(self):
        return self._getArray(0)

    def setSettingsList(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSettingsListType():
        return RandomBattlePopoverItemModel

    def _initialize(self):
        super(RandomBattlePopoverModel, self)._initialize()
        self._addArrayProperty('settingsList', Array())
        self.onItemChanged = self._addCommand('onItemChanged')