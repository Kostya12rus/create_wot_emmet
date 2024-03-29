# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/roles_view_model.py
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.tooltips.role_action_model import RoleActionModel

class RolesViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RolesViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def roleActions(self):
        return self._getViewModel(0)

    @staticmethod
    def getRoleActionsType():
        return RoleActionModel

    def getRoleType(self):
        return self._getString(1)

    def setRoleType(self, value):
        self._setString(1, value)

    def getRoleBgImage(self):
        return self._getResource(2)

    def setRoleBgImage(self, value):
        self._setResource(2, value)

    def getIsRoleActionsEnabled(self):
        return self._getBool(3)

    def setIsRoleActionsEnabled(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(RolesViewModel, self)._initialize()
        self._addViewModelProperty('roleActions', UserListModel())
        self._addStringProperty('roleType', '')
        self._addResourceProperty('roleBgImage', R.invalid())
        self._addBoolProperty('isRoleActionsEnabled', True)