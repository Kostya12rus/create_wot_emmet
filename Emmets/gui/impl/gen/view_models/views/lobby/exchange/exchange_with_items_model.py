# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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