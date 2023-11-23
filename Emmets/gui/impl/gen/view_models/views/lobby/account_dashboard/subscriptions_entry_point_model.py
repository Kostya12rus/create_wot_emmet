# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_dashboard/subscriptions_entry_point_model.py
from frameworks.wulf import ViewModel

class SubscriptionsEntryPointModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=1, commands=1):
        super(SubscriptionsEntryPointModel, self).__init__(properties=properties, commands=commands)

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(SubscriptionsEntryPointModel, self)._initialize()
        self._addBoolProperty('isEnabled', True)
        self.onClick = self._addCommand('onClick')