# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_new_tankman_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel

class RecruitNewTankmanDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(RecruitNewTankmanDialogModel, self).__init__(properties=properties, commands=commands)

    def getRole(self):
        return self._getString(6)

    def setRole(self, value):
        self._setString(6, value)

    def getVehicleName(self):
        return self._getString(7)

    def setVehicleName(self, value):
        self._setString(7, value)

    def getIsPremium(self):
        return self._getBool(8)

    def setIsPremium(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(RecruitNewTankmanDialogModel, self)._initialize()
        self._addStringProperty('role', '')
        self._addStringProperty('vehicleName', '')
        self._addBoolProperty('isPremium', False)