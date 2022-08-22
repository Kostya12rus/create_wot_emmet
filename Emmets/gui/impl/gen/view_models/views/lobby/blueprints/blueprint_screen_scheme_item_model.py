# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_screen_scheme_item_model.py
from frameworks.wulf import ViewModel

class BlueprintScreenSchemeItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BlueprintScreenSchemeItemModel, self).__init__(properties=properties, commands=commands)

    def getReceived(self):
        return self._getBool(0)

    def setReceived(self, value):
        self._setBool(0, value)

    def getIsNew(self):
        return self._getBool(1)

    def setIsNew(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(BlueprintScreenSchemeItemModel, self)._initialize()
        self._addBoolProperty('received', False)
        self._addBoolProperty('isNew', False)