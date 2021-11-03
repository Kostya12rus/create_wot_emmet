# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/select_slot_spec_dialog_model.py
from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.common.dialog_with_exchange import DialogWithExchange
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_content_model import SelectSlotSpecDialogContentModel

class SelectSlotSpecDialogModel(DialogWithExchange):
    __slots__ = ()
    BUY_NOT_REQUIRED_PANEL = 'buyNotRequiredPanel'

    def __init__(self, properties=17, commands=3):
        super(SelectSlotSpecDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def changePrice(self):
        return self._getViewModel(15)

    @property
    def mainContent(self):
        return self._getViewModel(16)

    def _initialize(self):
        super(SelectSlotSpecDialogModel, self)._initialize()
        self._addViewModelProperty('changePrice', PriceModel())
        self._addViewModelProperty('mainContent', SelectSlotSpecDialogContentModel())