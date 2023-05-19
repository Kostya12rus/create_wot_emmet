# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/collection/tooltips/collection_item_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.collection.collections_helpers import getItemResKey, getCollectionRes, getItemName, getImagePath
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.collection.tooltips.collection_item_tooltip_view_model import CollectionItemTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import ICollectionsSystemController

class CollectionItemTooltipView(ViewImpl):
    __slots__ = ('__collectionId', '__item')
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, itemId, collectionId, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.collection.tooltips.CollectionItemTooltipView())
        settings.model = CollectionItemTooltipViewModel()
        settings.args = args
        settings.kwargs = kwargs
        self.__collectionId = collectionId
        self.__item = self.__collectionsSystem.getCollectionItem(self.__collectionId, itemId)
        super(CollectionItemTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CollectionItemTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CollectionItemTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setName(getItemName(self.__collectionId, self.__item, collectionsSystem=self.__collectionsSystem))
            model.setImagePath(self.__getImage())
            model.setDescription(self.__getDescription())
            model.setIsReceived(self.__collectionsSystem.isItemReceived(self.__collectionId, self.__item.itemId))

    def __getDescription(self):
        itemRes = getCollectionRes(self.__collectionId, collectionsSystem=self.__collectionsSystem).item
        isItemAvailable = self.__collectionsSystem.isRelatedEventActive(self.__collectionId)
        conditionRes = itemRes.condition.available if isItemAvailable else itemRes.condition.unavailable
        return backport.text(conditionRes.dyn(getItemResKey(self.__collectionId, self.__item))())

    def __getImage(self):
        return getImagePath(R.images.gui.maps.icons.collectionItems.c_296x222.dyn(getItemResKey(self.__collectionId, self.__item)))