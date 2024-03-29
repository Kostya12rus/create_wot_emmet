# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/contents/multiple_items_content_to_upgrade.py
import typing
from gui.impl.lobby.dialogs.contents.multiple_items_content import MultipleItemsContent
from gui.impl.lobby.dialogs.auxiliary.confirmed_items_packer import ConfirmedItemsToUpgradePacker
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel

class MultipleItemsContentToUpgrade(MultipleItemsContent):
    __slots__ = ()

    def __init__(self, viewModel, items, vehicleInvID=None, itemsType=None):
        super(MultipleItemsContentToUpgrade, self).__init__(viewModel, items, vehicleInvID, itemsType)
        self._confirmedItemsPacker = ConfirmedItemsToUpgradePacker(vehicleInvID=vehicleInvID)