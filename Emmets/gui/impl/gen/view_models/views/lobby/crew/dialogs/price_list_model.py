# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/price_list_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.price_card_model import PriceCardModel

class PriceListModel(ViewModel):
    __slots__ = ('onCardClick', )

    def __init__(self, properties=1, commands=1):
        super(PriceListModel, self).__init__(properties=properties, commands=commands)

    def getCardsList(self):
        return self._getArray(0)

    def setCardsList(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCardsListType():
        return PriceCardModel

    def _initialize(self):
        super(PriceListModel, self)._initialize()
        self._addArrayProperty('cardsList', Array())
        self.onCardClick = self._addCommand('onCardClick')