# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lunar_ny/main_view/store_envelopes/received_envelope_model.py
from frameworks.wulf import ViewModel

class ReceivedEnvelopeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ReceivedEnvelopeModel, self).__init__(properties=properties, commands=commands)

    def getPlayerID(self):
        return self._getNumber(0)

    def setPlayerID(self, value):
        self._setNumber(0, value)

    def getPlayerName(self):
        return self._getString(1)

    def setPlayerName(self, value):
        self._setString(1, value)

    def getAmount(self):
        return self._getNumber(2)

    def setAmount(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(ReceivedEnvelopeModel, self)._initialize()
        self._addNumberProperty('playerID', 0)
        self._addStringProperty('playerName', '')
        self._addNumberProperty('amount', 0)