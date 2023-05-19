# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/window_view.py
from frameworks.wulf import View, ViewFlags, ViewSettings
from gui.impl.gen.view_models.windows.window_model import WindowModel
from gui.impl.gen import R

class WindowView(View):
    __slots__ = ()

    def __init__(self, layoutID=R.views.common.standard_window.standard_window.StandardWindow(), flags=ViewFlags.WINDOW_DECORATOR, viewModelClazz=WindowModel):
        super(WindowView, self).__init__(ViewSettings(layoutID, flags, viewModelClazz()))

    @property
    def viewModel(self):
        return super(WindowView, self).getViewModel()