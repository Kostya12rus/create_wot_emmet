# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/recruit_window/recruit_icon_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel

class RecruitIconViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RecruitIconViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def icon(self):
        return self._getViewModel(0)

    @staticmethod
    def getIconType():
        return IconViewModel

    @property
    def bgIcon(self):
        return self._getViewModel(1)

    @staticmethod
    def getBgIconType():
        return IconViewModel

    def _initialize(self):
        super(RecruitIconViewModel, self)._initialize()
        self._addViewModelProperty('icon', IconViewModel())
        self._addViewModelProperty('bgIcon', IconViewModel())