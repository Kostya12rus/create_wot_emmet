# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/comp7_header_model.py
from gui.impl.gen.view_models.views.lobby.platoon.comp7_member_count_dropdown import Comp7MemberCountDropdown
from gui.impl.gen.view_models.views.lobby.platoon.window_header_model import WindowHeaderModel

class Comp7HeaderModel(WindowHeaderModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(Comp7HeaderModel, self).__init__(properties=properties, commands=commands)

    @property
    def memberCountDropdown(self):
        return self._getViewModel(7)

    @staticmethod
    def getMemberCountDropdownType():
        return Comp7MemberCountDropdown

    def _initialize(self):
        super(Comp7HeaderModel, self)._initialize()
        self._addViewModelProperty('memberCountDropdown', Comp7MemberCountDropdown())