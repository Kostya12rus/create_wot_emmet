# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/main_content/ammunition_buy_content.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel

class AmmunitionBuyContent(MultipleItemsContentModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(AmmunitionBuyContent, self).__init__(properties=properties, commands=commands)

    def getLacksItem(self):
        return self._getArray(2)

    def setLacksItem(self, value):
        self._setArray(2, value)

    @staticmethod
    def getLacksItemType():
        return unicode

    def getDemountPairModification(self):
        return self._getBool(3)

    def setDemountPairModification(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(AmmunitionBuyContent, self)._initialize()
        self._addArrayProperty('lacksItem', Array())
        self._addBoolProperty('demountPairModification', False)