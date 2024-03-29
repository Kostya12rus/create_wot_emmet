# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/shells_setup_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.shell_slot_model import ShellSlotModel

class ShellsSetupModel(BaseSetupModel):
    __slots__ = ('onShellUpdate', )

    def __init__(self, properties=10, commands=8):
        super(ShellsSetupModel, self).__init__(properties=properties, commands=commands)

    def getShellsTempString(self):
        return self._getString(5)

    def setShellsTempString(self, value):
        self._setString(5, value)

    def getInstalledCount(self):
        return self._getNumber(6)

    def setInstalledCount(self, value):
        self._setNumber(6, value)

    def getMaxCount(self):
        return self._getNumber(7)

    def setMaxCount(self, value):
        self._setNumber(7, value)

    def getClipCount(self):
        return self._getNumber(8)

    def setClipCount(self, value):
        self._setNumber(8, value)

    def getSlots(self):
        return self._getArray(9)

    def setSlots(self, value):
        self._setArray(9, value)

    @staticmethod
    def getSlotsType():
        return ShellSlotModel

    def _initialize(self):
        super(ShellsSetupModel, self)._initialize()
        self._addStringProperty('shellsTempString', '')
        self._addNumberProperty('installedCount', 0)
        self._addNumberProperty('maxCount', 0)
        self._addNumberProperty('clipCount', 1)
        self._addArrayProperty('slots', Array())
        self.onShellUpdate = self._addCommand('onShellUpdate')