# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/windows/simple_dialog_window_model.py
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class SimpleDialogWindowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SimpleDialogWindowModel, self).__init__(properties=properties, commands=commands)

    def getMessage(self):
        return self._getResource(0)

    def setMessage(self, value):
        self._setResource(0, value)

    def getFormattedMessage(self):
        return self._getString(1)

    def setFormattedMessage(self, value):
        self._setString(1, value)

    def getMessageArgs(self):
        return self._getArray(2)

    def setMessageArgs(self, value):
        self._setArray(2, value)

    def getMessageFmtArgs(self):
        return self._getArray(3)

    def setMessageFmtArgs(self, value):
        self._setArray(3, value)

    def getIsMessageFmtArgsNamed(self):
        return self._getBool(4)

    def setIsMessageFmtArgsNamed(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(SimpleDialogWindowModel, self)._initialize()
        self._addResourceProperty('message', R.invalid())
        self._addStringProperty('formattedMessage', '')
        self._addArrayProperty('messageArgs', Array())
        self._addArrayProperty('messageFmtArgs', Array())
        self._addBoolProperty('isMessageFmtArgsNamed', True)