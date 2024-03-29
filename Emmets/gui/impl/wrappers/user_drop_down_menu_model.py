# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/wrappers/user_drop_down_menu_model.py
import logging
from gui.impl.gen.view_models.ui_kit.drop_down_menu_item_model import DropDownMenuItemModel
from gui.impl.wrappers.user_list_model import UserListModel
_logger = logging.getLogger(__name__)

class UserDropDownMenuModel(UserListModel):
    __slots__ = ()

    def addItem(self, actionID, label, icon=None, isEnabled=True):
        item = DropDownMenuItemModel()
        item.setId(actionID)
        item.setLabel(label)
        item.setIsEnabled(isEnabled)
        if icon is not None:
            item.setIcon(icon)
        self.getItems().addViewModel(item)
        return

    def getItemByID(self, actionID):
        try:
            return next(item for item in self.getItems() if item.getId() == actionID)
        except StopIteration:
            _logger.error("Item with actionID '%d' is not found in drop down list", actionID)
            return

        return