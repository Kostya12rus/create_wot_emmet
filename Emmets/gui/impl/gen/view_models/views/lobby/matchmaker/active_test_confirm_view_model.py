# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/matchmaker/active_test_confirm_view_model.py
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel

class ActiveTestConfirmViewModel(FullScreenDialogWindowModel):
    __slots__ = ('onOpenPortalClicked', )

    def __init__(self, properties=14, commands=4):
        super(ActiveTestConfirmViewModel, self).__init__(properties=properties, commands=commands)

    def getClusterName(self):
        return self._getString(11)

    def setClusterName(self, value):
        self._setString(11, value)

    def getTimeRangeStart(self):
        return self._getNumber(12)

    def setTimeRangeStart(self, value):
        self._setNumber(12, value)

    def getTimeRangeEnd(self):
        return self._getNumber(13)

    def setTimeRangeEnd(self, value):
        self._setNumber(13, value)

    def _initialize(self):
        super(ActiveTestConfirmViewModel, self)._initialize()
        self._addStringProperty('clusterName', '')
        self._addNumberProperty('timeRangeStart', 0)
        self._addNumberProperty('timeRangeEnd', 0)
        self.onOpenPortalClicked = self._addCommand('onOpenPortalClicked')