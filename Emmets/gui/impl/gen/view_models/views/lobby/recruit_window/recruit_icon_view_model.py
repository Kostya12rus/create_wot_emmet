# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/recruit_window/recruit_icon_view_model.py
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