# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/missions/bonuses/icon_bonus_model.py
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class IconBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(IconBonusModel, self).__init__(properties=properties, commands=commands)

    def getIcon(self):
        return self._getString(7)

    def setIcon(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(IconBonusModel, self)._initialize()
        self._addStringProperty('icon', '')