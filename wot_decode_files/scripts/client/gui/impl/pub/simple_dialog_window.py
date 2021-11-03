# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/pub/simple_dialog_window.py
import typing
from frameworks.wulf import ViewModel, ViewSettings
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets
from gui.impl.gen.view_models.windows.simple_dialog_window_model import SimpleDialogWindowModel
from gui.impl.pub.dialog_window import DialogContent, DialogFlags
from gui.impl.pub.pure_dialog_window import PureDialogWindow

class SimpleDialogWindow(PureDialogWindow):

    def __init__(self, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, preset=DialogPresets.DEFAULT, flags=DialogFlags.TOP_WINDOW):
        contentSettings = ViewSettings(R.views.common.dialog_view.simple_dialog_content.SimpleDialogContent())
        contentSettings.model = SimpleDialogWindowModel()
        super(SimpleDialogWindow, self).__init__(bottomContent=bottomContent, parent=parent, balanceContent=balanceContent, enableBlur=enableBlur, content=DialogContent(contentSettings), flags=flags)
        self._setPreset(preset)

    @property
    def contentViewModel(self):
        content = self.content
        if content is not None:
            return content.getViewModel()
        else:
            return

    def setFormattedMessage(self, formattedMessage=''):
        if formattedMessage != '':
            self.contentViewModel.setFormattedMessage(formattedMessage)

    def setMessage(self, message, args=None, fmtArgs=None, namedFmtArgs=True):
        model = self.contentViewModel
        model.setMessage(message)
        if fmtArgs:
            self._addArgsOfModel(model.getMessageFmtArgs(), fmtArgs)
            model.setIsMessageFmtArgsNamed(namedFmtArgs)
        elif args:
            self._addArgsOfString(model.getMessageArgs(), args)