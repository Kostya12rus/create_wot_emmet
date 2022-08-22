# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/cn_loot_boxes/china_loot_boxes_open_box_error_view.py
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.cn_loot_boxes.china_loot_boxes_open_box_error_view_model import ChinaLootBoxesOpenBoxErrorViewModel
from gui.impl.pub import ViewImpl, WindowImpl
from PlayerEvents import g_playerEvents

class ChinaLootBoxesOpenBoxErrorView(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.model = ChinaLootBoxesOpenBoxErrorViewModel()
        super(ChinaLootBoxesOpenBoxErrorView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ChinaLootBoxesOpenBoxErrorView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        g_playerEvents.onDisconnected += self.__onDisconnected

    def _finalize(self):
        g_playerEvents.onDisconnected -= self.__onDisconnected

    def __onDisconnected(self):
        self.destroyWindow()


class ChinaLootBoxesOpenBoxErrorWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, parent=None):
        super(ChinaLootBoxesOpenBoxErrorWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=ChinaLootBoxesOpenBoxErrorView(R.views.lobby.cn_loot_boxes.ChinaLootBoxesOpenBoxErrorView()), parent=parent)