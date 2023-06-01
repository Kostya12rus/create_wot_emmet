# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/sub_views/frontline_confirm_title.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.frontline_confirm_title_model import FrontlineConfirmTitleModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class FrontlineConfirmTitle(ViewImpl):
    __slots__ = ('_title', )
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.tanksetup.dialogs.sub_views.FrontlineConfirmTitle

    def __init__(self, title):
        settings = ViewSettings(self._LAYOUT_DYN_ACCESSOR())
        settings.model = FrontlineConfirmTitleModel()
        self._title = title
        super(FrontlineConfirmTitle, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FrontlineConfirmTitle, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (vm):
            vm.setTitle(self._title)