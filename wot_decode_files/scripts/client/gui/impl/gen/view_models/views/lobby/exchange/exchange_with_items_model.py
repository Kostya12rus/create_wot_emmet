# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/exchange/exchange_with_items_model.py
from gui.impl.gen.view_models.views.lobby.common.dialog_with_exchange import DialogWithExchange
from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel

class ExchangeWithItemsModel(DialogWithExchange):
    __slots__ = ()

    def __init__(self, properties=16, commands=3):
        super(ExchangeWithItemsModel, self).__init__(properties=properties, commands=commands)

    @property
    def mainContent(self):
        return self._getViewModel(15)

    @staticmethod
    def getMainContentType():
        return MultipleItemsContentModel

    def _initialize(self):
        super(ExchangeWithItemsModel, self)._initialize()
        self._addViewModelProperty('mainContent', MultipleItemsContentModel())