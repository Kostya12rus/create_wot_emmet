# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/dialogs/install_to_unprofitable_slot_dialog_builder.py
from gui.impl.dialogs.dialog_template_button import ButtonPresenter, ConfirmButton
from gui.impl.dialogs.gf_builders import BaseDialogBuilder
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType
from gui.impl.pub.dialog_window import DialogButtons

class InstallToUnprofitableSlotDialogBuilder(BaseDialogBuilder):

    def __init__(self):
        super(InstallToUnprofitableSlotDialogBuilder, self).__init__()
        stringsPath = R.strings.ny.dialogs.unprofitableSlot
        iconPath = R.images.gui.maps.uiKit.dialogs
        self.setIcon(iconPath.icons.info(), [iconPath.highlights.blue()])
        self.setTitle(stringsPath.title())
        self.setDescription(stringsPath.description())
        self.addButton(ConfirmButton(stringsPath.button.getMore()))
        self.setFocusedButtonID(DialogButtons.SUBMIT)
        self.addButton(ButtonPresenter(stringsPath.button.leave(), DialogButtons.INSTALL, ButtonType.SECONDARY))