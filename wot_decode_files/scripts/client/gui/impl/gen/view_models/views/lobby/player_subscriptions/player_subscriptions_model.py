# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/player_subscriptions/player_subscriptions_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription import Subscription

class PlayerSubscriptionsModel(ViewModel):
    __slots__ = ('onBack', 'onCardClick', 'onButtonClick')

    def __init__(self, properties=2, commands=3):
        super(PlayerSubscriptionsModel, self).__init__(properties=properties, commands=commands)

    def getSubscriptions(self):
        return self._getArray(0)

    def setSubscriptions(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSubscriptionsType():
        return Subscription

    def getWarningTitle(self):
        return self._getResource(1)

    def setWarningTitle(self, value):
        self._setResource(1, value)

    def _initialize(self):
        super(PlayerSubscriptionsModel, self)._initialize()
        self._addArrayProperty('subscriptions', Array())
        self._addResourceProperty('warningTitle', R.invalid())
        self.onBack = self._addCommand('onBack')
        self.onCardClick = self._addCommand('onCardClick')
        self.onButtonClick = self._addCommand('onButtonClick')