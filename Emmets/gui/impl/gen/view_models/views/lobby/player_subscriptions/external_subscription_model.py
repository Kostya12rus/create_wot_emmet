# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/player_subscriptions/external_subscription_model.py
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionModel

class ExternalSubscriptionModel(SubscriptionModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(ExternalSubscriptionModel, self).__init__(properties=properties, commands=commands)

    def getHas3rdPartyRewardsToClaim(self):
        return self._getBool(8)

    def setHas3rdPartyRewardsToClaim(self, value):
        self._setBool(8, value)

    def getHasDepotRewardsToClaim(self):
        return self._getBool(9)

    def setHasDepotRewardsToClaim(self, value):
        self._setBool(9, value)

    def _initialize(self):
        super(ExternalSubscriptionModel, self)._initialize()
        self._addBoolProperty('has3rdPartyRewardsToClaim', True)
        self._addBoolProperty('hasDepotRewardsToClaim', True)