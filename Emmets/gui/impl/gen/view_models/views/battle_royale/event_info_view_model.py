# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/event_info_view_model.py
from frameworks.wulf import ViewModel

class EventInfoViewModel(ViewModel):
    __slots__ = ('onInfoVideoClicked', )

    def __init__(self, properties=1, commands=1):
        super(EventInfoViewModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(EventInfoViewModel, self)._initialize()
        self._addStringProperty('title', '')
        self.onInfoVideoClicked = self._addCommand('onInfoVideoClicked')