# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/demo_renaming_unavailable_overlay_view.py
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.error_model import ErrorModel
from gui.impl.lobby.account_completion.common.base_overlay_view import BaseOverlayView

class DemoRenamingUnavailableOverlayView(BaseOverlayView):
    __slots__ = ()
    _IS_CLOSE_BUTTON_VISIBLE = False
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.account_completion.ErrorView
    _VIEW_MODEL_CLASS = ErrorModel

    @property
    def viewModel(self):
        return super(DemoRenamingUnavailableOverlayView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(DemoRenamingUnavailableOverlayView, self)._onLoading(*args, **kwargs)
        self.viewModel.setMessage(backport.text(R.strings.dialogs.accountCompletion.error.renamingNotAvailable()))
        self.viewModel.setButtonLabel(R.strings.dialogs.accountCompletion.error.button.c_continue())

    def activate(self, *args, **kwargs):
        super(DemoRenamingUnavailableOverlayView, self).activate(*args, **kwargs)
        self.viewModel.onButtonClicked += self._closeClickedHandler

    def deactivate(self):
        super(DemoRenamingUnavailableOverlayView, self).deactivate()
        self.viewModel.onButtonClicked -= self._closeClickedHandler