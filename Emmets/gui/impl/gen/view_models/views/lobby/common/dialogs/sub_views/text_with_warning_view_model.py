# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/dialogs/sub_views/text_with_warning_view_model.py
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