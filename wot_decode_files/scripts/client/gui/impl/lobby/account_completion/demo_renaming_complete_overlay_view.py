# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/demo_renaming_complete_overlay_view.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.renaming_complete_model import RenamingCompleteModel
from gui.impl.lobby.account_completion.common.base_overlay_view import BaseOverlayView

class DemoRenamingCompleteOverlayView(BaseOverlayView):
    __slots__ = ()
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.account_completion.RenamingCompleteView
    _VIEW_MODEL_CLASS = RenamingCompleteModel
    _IS_CLOSE_BUTTON_VISIBLE = False

    @property
    def viewModel(self):
        return super(DemoRenamingCompleteOverlayView, self).getViewModel()

    def activate(self, name, *args, **kwargs):
        super(DemoRenamingCompleteOverlayView, self).activate(*args, **kwargs)
        self.viewModel.setName(name)

    def _onLoading(self, *args, **kwargs):
        super(DemoRenamingCompleteOverlayView, self)._onLoading(*args, **kwargs)
        self.viewModel.setTitle(R.strings.dialogs.accountCompletion.renamingCompleteOverlay.title())
        self.viewModel.setSubTitle(R.strings.dialogs.accountCompletion.renamingCompleteOverlay.subTitle())