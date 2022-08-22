# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_royale/dialogs/sub_views/text_with_warning_view_model.py
from frameworks.wulf import ViewModel

class TextWithWarningViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TextWithWarningViewModel, self).__init__(properties=properties, commands=commands)

    def getMainText(self):
        return self._getString(0)

    def setMainText(self, value):
        self._setString(0, value)

    def getWarningText(self):
        return self._getString(1)

    def setWarningText(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(TextWithWarningViewModel, self)._initialize()
        self._addStringProperty('mainText', '')
        self._addStringProperty('warningText', '')