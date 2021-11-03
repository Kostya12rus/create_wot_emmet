# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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