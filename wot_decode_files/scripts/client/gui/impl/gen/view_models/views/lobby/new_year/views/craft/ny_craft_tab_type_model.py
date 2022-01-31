# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/views/craft/ny_craft_tab_type_model.py
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.craft.ny_craft_tab_type_item_model import NyCraftTabTypeItemModel

class NyCraftTabTypeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyCraftTabTypeModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getTypes(self):
        return self._getArray(1)

    def setTypes(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(NyCraftTabTypeModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addArrayProperty('types', Array())