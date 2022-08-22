# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/subscription/subscription_award_view_model.py
from frameworks.wulf import ViewModel

class SubscriptionAwardViewModel(ViewModel):
    __slots__ = ('onCloseButtonClick', 'onInfoButtonClick')

    def __init__(self, properties=1, commands=2):
        super(SubscriptionAwardViewModel, self).__init__(properties=properties, commands=commands)

    def getNextCharge(self):
        return self._getNumber(0)

    def setNextCharge(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(SubscriptionAwardViewModel, self)._initialize()
        self._addNumberProperty('nextCharge', 0)
        self.onCloseButtonClick = self._addCommand('onCloseButtonClick')
        self.onInfoButtonClick = self._addCommand('onInfoButtonClick')