# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/bonuses/blueprint_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class BlueprintBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(BlueprintBonusModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(8)

    def setType(self, value):
        self._setString(8, value)

    def _initialize(self):
        super(BlueprintBonusModel, self)._initialize()
        self._addStringProperty('type', '')