# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/dialogs/sub_views/content/text_warning_content.py
from frameworks.wulf import ViewSettings
from gui.impl.dialogs.dialog_template_utils import toString
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.dialogs.sub_views.text_with_warning_view_model import TextWithWarningViewModel
from gui.impl.pub import ViewImpl

class TextWithWarning(ViewImpl):
    __slots__ = ()

    def __init__(self, mainText, warningText=None):
        settings = ViewSettings(R.views.dialogs.sub_views.content.TextWithWarning())
        settings.model = TextWithWarningViewModel()
        settings.kwargs = {'mainText': mainText, 
           'warningText': warningText}
        super(TextWithWarning, self).__init__(settings)

    def _onLoading(self, mainText, warningText, *args, **kwargs):
        super(TextWithWarning, self)._onLoading(*args, **kwargs)
        viewModel = self.getViewModel()
        viewModel.setMainText(toString(mainText))
        if warningText:
            viewModel.setWarningText(toString(warningText))

    def updateText(self, text):
        self.getViewModel().setText(toString(text))