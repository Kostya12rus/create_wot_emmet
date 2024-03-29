# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/contents/checkbox_content.py
from frameworks.wulf import ViewSettings
from gui.impl.gen.resources import R
from gui.impl.pub.dialog_window import DialogContent
from gui.impl.gen.view_models.ui_kit.check_box_model import CheckBoxModel

class CheckBoxDialogContent(DialogContent):

    def __init__(self, label, selected=False):
        settings = ViewSettings(R.views.common.dialog_view.components.checkbox_content.CheckBoxDialogContent())
        settings.model = CheckBoxModel()
        settings.args = (label, selected)
        super(CheckBoxDialogContent, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CheckBoxDialogContent, self).getViewModel()

    def _onLoading(self, label, selected):
        super(CheckBoxDialogContent, self)._onLoading()
        with self.getViewModel().transaction() as (model):
            model.setLabel(label)
            model.setIsSelected(selected)
        self.viewModel.onSelected += self.__onCheckBoxSelected

    def _finalize(self):
        self.viewModel.onSelected -= self.__onCheckBoxSelected
        super(CheckBoxDialogContent, self)._finalize()

    def __onCheckBoxSelected(self, args=None):
        with self.getViewModel().transaction() as (model):
            model.setIsSelected(args['selected'])