# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/piggy_bank/piggy_bank_states.py
from enum import Enum
from frameworks.wulf import ViewModel

class BankState(Enum):
    AVAILABLE = 'available'
    ACTIVE = 'active'
    DISABLE = 'disable'


class PiggyBankStates(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(PiggyBankStates, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(PiggyBankStates, self)._initialize()