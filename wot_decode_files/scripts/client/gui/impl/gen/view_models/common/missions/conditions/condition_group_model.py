# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/conditions/condition_group_model.py
from gui.impl.gen.view_models.common.missions.conditions.condition_base_model import ConditionBaseModel

class ConditionGroupModel(ConditionBaseModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ConditionGroupModel, self).__init__(properties=properties, commands=commands)

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(ConditionGroupModel, self)._initialize()
        self._addArrayProperty('items')