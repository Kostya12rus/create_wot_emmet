# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/dialogs/reset_loot_box_statistics_builder.py
from frameworks.wulf import WindowLayer
from gui.impl.dialogs.gf_builders import ConfirmCancelDialogBuilder
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper

class ResetLootBoxStatisticsBuilder(ConfirmCancelDialogBuilder):

    def build(self, withBlur=False):
        return FullScreenDialogWindowWrapper(self.buildView(), doBlur=withBlur, layer=WindowLayer.OVERLAY)