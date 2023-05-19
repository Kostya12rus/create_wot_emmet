# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/select_demount_kit_view_model.py
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectDemountKitViewModel(SelectOptionBaseItemViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(SelectDemountKitViewModel, self).__init__(properties=properties, commands=commands)

    def getStorageCount(self):
        return self._getNumber(4)

    def setStorageCount(self, value):
        self._setNumber(4, value)

    def getText(self):
        return self._getString(5)

    def setText(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(SelectDemountKitViewModel, self)._initialize()
        self._addNumberProperty('storageCount', 0)
        self._addStringProperty('text', '')