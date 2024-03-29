# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/storage/forsell/forsell_cm_handlers.py
from adisp import adisp_process
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import option, CMLabel, ContextMenu
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared import event_dispatcher as shared_events
from ids_generators import SequenceIDGenerator
from gui.shared.event_dispatcher import showConfirmInStorageDialog

class ForSellCMHandler(ContextMenu, EventSystemEntity):
    __sqGen = SequenceIDGenerator()

    @option(__sqGen.next(), CMLabel.INFORMATION)
    def showInfo(self):
        shared_events.showStorageModuleInfo(self._id)

    @option(__sqGen.next(), CMLabel.SELL)
    @adisp_process
    def sell(self):
        showConfirmInStorageDialog(self._id)

    @option(__sqGen.next(), CMLabel.SALE_OPTION)
    def switchSaleOption(self):
        self.fireEvent(events.StorageEvent(events.StorageEvent.SELECT_MODULE_FOR_SELL, ctx={'intCD': self._id}), scope=EVENT_BUS_SCOPE.LOBBY)

    def _getOptionCustomData(self, label):
        optionData = super(ForSellCMHandler, self)._getOptionCustomData(label)
        if label == CMLabel.SALE_OPTION:
            optionData.label = 'prohibitSale' if self._selected else 'allowSale'
        return optionData

    def _initFlashValues(self, ctx):
        super(ForSellCMHandler, self)._initFlashValues(ctx)
        self._selected = ctx.selected