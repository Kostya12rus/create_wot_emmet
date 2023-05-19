# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/player_subscriptions/wot_subscription_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionModel

class WotSubscriptionStateEnum(Enum):
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'


class WotSubscriptionModel(SubscriptionModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(WotSubscriptionModel, self).__init__(properties=properties, commands=commands)

    def getWotSubscriptionState(self):
        return WotSubscriptionStateEnum(self._getString(8))

    def setWotSubscriptionState(self, value):
        self._setString(8, value.value)

    def _initialize(self):
        super(WotSubscriptionModel, self)._initialize()
        self._addStringProperty('wotSubscriptionState')