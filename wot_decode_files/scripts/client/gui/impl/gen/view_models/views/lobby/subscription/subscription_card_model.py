# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/subscription/subscription_card_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class SubscriptionCardState(Enum):
    AVAILABLE = 'available'
    ACTIVE = 'active'
    DISABLE = 'disable'


class SubscriptionCardModel(ViewModel):
    __slots__ = ('onCardClick', 'onInfoButtonClik')

    def __init__(self, properties=2, commands=2):
        super(SubscriptionCardModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return SubscriptionCardState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def getNextCharge(self):
        return self._getString(1)

    def setNextCharge(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(SubscriptionCardModel, self)._initialize()
        self._addStringProperty('state')
        self._addStringProperty('nextCharge', '')
        self.onCardClick = self._addCommand('onCardClick')
        self.onInfoButtonClik = self._addCommand('onInfoButtonClik')