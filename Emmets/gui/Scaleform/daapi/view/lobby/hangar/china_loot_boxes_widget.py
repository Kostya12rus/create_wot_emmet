# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/china_loot_boxes_widget.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.cn_loot_boxes.china_loot_boxes_entry_point import ChinaLootBoxesEntryPointWidget

class ChinaLootBoxesWidget(InjectComponentAdaptor):

    def _makeInjectView(self):
        return ChinaLootBoxesEntryPointWidget()