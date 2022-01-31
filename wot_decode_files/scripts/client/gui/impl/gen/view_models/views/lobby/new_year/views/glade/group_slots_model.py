# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/views/glade/group_slots_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.new_year.views.glade.slot_model import SlotModel

class GroupSlotsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(GroupSlotsModel, self).__init__(properties=properties, commands=commands)

    @property
    def slots(self):
        return self._getViewModel(0)

    def _initialize(self):
        super(GroupSlotsModel, self)._initialize()
        self._addViewModelProperty('slots', UserListModel())