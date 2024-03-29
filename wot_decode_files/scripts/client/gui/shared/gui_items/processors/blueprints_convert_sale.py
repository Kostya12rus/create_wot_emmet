# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/processors/blueprints_convert_sale.py
import BigWorld
from gui.shared.gui_items.processors import Processor

class ProcessExchangeBlueprintsProcessor(Processor):

    def __init__(self, offerID, count=1):
        super(ProcessExchangeBlueprintsProcessor, self).__init__()
        self.offerID = offerID
        self.count = count

    def _request(self, callback):
        BigWorld.player().exchangeBlueprintsSale(self.offerID, self.count, (lambda code, errStr: self._response(code, callback, errStr=errStr)))