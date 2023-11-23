# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/sub_views/frontline_confirm_icons.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.frontline_confirm_icons_model import FrontlineConfirmIconsModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class FrontlineConfirmIcons(ViewImpl):
    __slots__ = ('_icons', '_isExtendedHeight')
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.tanksetup.dialogs.sub_views.FrontlineConfirmIcons

    def __init__(self, isExtendedHeight):
        settings = ViewSettings(self._LAYOUT_DYN_ACCESSOR())
        settings.model = FrontlineConfirmIconsModel()
        self._icons = []
        self._isExtendedHeight = isExtendedHeight
        super(FrontlineConfirmIcons, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FrontlineConfirmIcons, self).getViewModel()

    def addIcon(self, iconPath):
        self._icons.append(iconPath)

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (vm):
            vm.setIsExtendedHeight(self._isExtendedHeight)
            icons = vm.getIcons()
            icons.clear()
            for icon in self._icons:
                icons.addString(icon)