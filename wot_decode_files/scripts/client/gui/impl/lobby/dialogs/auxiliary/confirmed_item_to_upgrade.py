# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_item_to_upgrade.py
from gui.impl.lobby.dialogs.auxiliary.confirmed_item import ConfirmedItem, ConfirmedArtefact, ConfirmedOptDevice
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_helpers import getOverlayTypeByItem
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA

class ConfirmedItemToUpgrade(ConfirmedItem):

    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        if item.itemTypeID in GUI_ITEM_TYPE.ARTEFACTS:
            return ConfirmedArtefactToUpgrade.createFromGUIItem(item, ctx)
        return super(ConfirmedItemToUpgrade, cls).createFromGUIItem(item)


class ConfirmedArtefactToUpgrade(ConfirmedArtefact):

    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
            return ConfirmedOptDeviceToUpgrade(item, ctx)
        return super(ConfirmedArtefactToUpgrade, cls).createFromGUIItem(item, ctx)


class ConfirmedOptDeviceToUpgrade(ConfirmedOptDevice):

    def getOverlayType(self):
        return getOverlayTypeByItem(self._item, self.__getOptDeviceCriteria())

    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        return ConfirmedOptDeviceToUpgrade(item, ctx)

    @staticmethod
    def __getOptDeviceCriteria():
        return {ItemHighlightTypes.TROPHY_UPGRADED: REQ_CRITERIA.ITEM_TYPES(GUI_ITEM_TYPE.OPTIONALDEVICE) | REQ_CRITERIA.OPTIONAL_DEVICE.TROPHY | REQ_CRITERIA.CUSTOM((lambda i: i.isUpgradable or i.isUpgraded)), 
           ItemHighlightTypes.TROPHY_BASIC: REQ_CRITERIA.NONE}