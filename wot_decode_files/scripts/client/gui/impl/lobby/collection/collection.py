# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/collection/collection.py
from functools import partial
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from shared_utils import first
from account_helpers import AccountSettings
from account_helpers.AccountSettings import IS_BATTLE_PASS_COLLECTION_SEEN
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, ViewStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.collection.collections_helpers import composeBonuses, getImagePath, getItemResKey, getShownNewItemsCount, isItemNew, isRewardNew, setItemShown, setRewardShown, setShownNewItemsCount, showCollectionStylePreview, setCollectionTutorialCompleted, isTutorialCompleted
from gui.collection.sounds import COLLECTIONS_SOUND_SPACE, Sounds
from gui.impl import backport
from gui.impl.auxiliary.collections_helper import getCollectionsBonusPacker
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.collection.collection_view_model import CollectionViewModel
from gui.impl.gen.view_models.views.lobby.collection.item_model import ItemModel, ItemState
from gui.impl.gen.view_models.views.lobby.collection.reward_info_model import RewardInfoModel, RewardState
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.collection.tooltips.collection_item_tooltip_view import CollectionItemTooltipView
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.event_dispatcher import showCollectionItemPreviewWindow, showCollectionWindow, showHangar
from helpers import dependency, isPlayerAccount
from items.components.c11n_components import splitIntDescr
from items.components.c11n_constants import CustomizationType
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import ICollectionsSystemController
from skeletons.gui.impl import IGuiLoader

class CollectionView(ViewImpl):
    __slots__ = ('__backCallback', '__backBtnText', '__collection', '__rewardTooltips')
    _COMMON_SOUND_SPACE = COLLECTIONS_SOUND_SPACE
    __appLoader = dependency.descriptor(IAppLoader)
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)
    __guiLoader = dependency.descriptor(IGuiLoader)

    def __init__(self, collectionId, backCallback, backBtnText):
        settings = ViewSettings(R.views.lobby.collection.CollectionView())
        settings.flags = ViewFlags.LOBBY_TOP_SUB_VIEW
        settings.model = CollectionViewModel()
        self.__backCallback = backCallback
        self.__backBtnText = backBtnText
        self.__collection = self.__collectionsSystem.getCollection(collectionId)
        self.__rewardTooltips = {}
        super(CollectionView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CollectionView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(CollectionView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.battle_pass.tooltips.BattlePassCoinTooltipView():
            return BattlePassCoinTooltipView()
        else:
            if contentID == R.views.lobby.collection.tooltips.CollectionItemTooltipView():
                if event.hasArgument('itemId'):
                    return CollectionItemTooltipView(itemId=event.getArgument('itemId'), collectionId=self.__collection.collectionId)
                tooltipData = self.getTooltipData(event)
                if tooltipData is not None:
                    return CollectionItemTooltipView(*tooltipData.specialArgs)
            return super(CollectionView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__rewardTooltips.get(tooltipId)

    def _onLoading(self, *args, **kwargs):
        super(CollectionView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setBackButtonText(self.__backBtnText)
            model.setIsCompleted(self.__collectionsSystem.isCollectionCompleted(self.__collection.collectionId))
            model.setCurrentCollection(self.__collection.name)
            model.setIsTutorial(not isTutorialCompleted(self.__collection.collectionId))
            self.__fillItems(model=model)
            self.__fillProgression(model=model)

    def _onLoaded(self, *args, **kwargs):
        super(CollectionView, self)._onLoaded(*args, **kwargs)
        if not AccountSettings.getSettings(IS_BATTLE_PASS_COLLECTION_SEEN):
            AccountSettings.setSettings(IS_BATTLE_PASS_COLLECTION_SEEN, True)
            g_eventBus.handleEvent(events.CollectionsEvent(events.CollectionsEvent.BATTLE_PASS_ENTRY_POINT_VISITED), scope=EVENT_BUS_SCOPE.LOBBY)

    def _finalize(self):

        def battlePassViewsPredicate(view):
            battlePassViews = (
             R.views.lobby.battle_pass.ChapterChoiceView(), R.views.lobby.battle_pass.BattlePassProgressionsView())
            return view.layoutID in battlePassViews and view.viewStatus == ViewStatus.LOADED

        if self.__guiLoader.windowsManager.findViews(battlePassViewsPredicate):
            self.soundManager.setState(Sounds.STATE_PLACE.value, Sounds.STATE_PLACE_TASKS.value)
        if callable(self.__backCallback) and isPlayerAccount():
            self.__backCallback()
        self.__backCallback = None
        self.__rewardTooltips = None
        super(CollectionView, self)._finalize()
        return

    def _getEvents(self):
        return (
         (
          self.__collectionsSystem.onServerSettingsChanged, self.__onSettingsChanged),
         (
          self.__collectionsSystem.onBalanceUpdated, self.__onBalanceUpdated),
         (
          self.viewModel.onSetItemReceived, self.__onSetItemReceived),
         (
          self.viewModel.onSetRewardReceived, self.__onSetRewardReceived),
         (
          self.viewModel.onSetProgressItemsReceived, self.__onSetProgressItemsReceived),
         (
          self.viewModel.onOpenItemPreview, self.__onOpenItemPreview),
         (
          self.viewModel.onFinishTutorial, self.__onFinishTutorial))

    @replaceNoneKwargsModel
    def __fillItems(self, model=None):
        itemModels = model.getItems()
        itemModels.clear()
        for item in self.__collection.items.itervalues():
            itemModel = ItemModel()
            self._filItemModel(item, itemModel)
            itemModels.addViewModel(itemModel)

        itemModels.invalidate()

    def _filItemModel(self, item, itemModel):
        itemId = item.itemId
        itemModel.setItemId(itemId)
        itemModel.setState(self.__getItemState(itemId))
        collectionId = self.__collection.collectionId
        itemResKey = getItemResKey(collectionId, item)
        itemModel.setReceivedImagePath(getImagePath(R.images.gui.maps.icons.collectionItems.received.dyn(itemResKey)))
        itemModel.setUnreceivedImagePath(getImagePath(R.images.gui.maps.icons.collectionItems.unreceived.dyn(itemResKey)))

    @replaceNoneKwargsModel
    def __fillProgression(self, model=None):
        self.__fillProgressInfo(model=model)
        self.__fillRewardsInfo(model=model)

    @replaceNoneKwargsModel
    def __fillProgressInfo(self, model=None):
        collectionId = self.__collection.collectionId
        receivedItemsCount = self.__collectionsSystem.getReceivedProgressItemCount(collectionId)
        model.setReceivedItemsCount(receivedItemsCount)
        model.setPrevReceivedItemsCount(min(getShownNewItemsCount(collectionId), receivedItemsCount))
        model.setMaxItemsCount(self.__collectionsSystem.getMaxProgressItemCount(collectionId))

    @replaceNoneKwargsModel
    def __fillRewardsInfo(self, model=None):
        rewardItems = sorted(self.__collection.rewards.items(), key=(lambda (reqCount, _): reqCount))
        rewardInfoModels = model.getRewardsInfo()
        rewardInfoModels.clear()
        self.__rewardTooltips.clear()
        for requiredCount, rewards in rewardItems:
            rewardInfoModel = RewardInfoModel()
            rewardInfoModel.setRequiredItemsCount(requiredCount)
            rewardInfoModel.setState(self.__getRewardState(requiredCount))
            packBonusModelAndTooltipData(composeBonuses([rewards]), rewardInfoModel.getRewards(), self.__rewardTooltips, getCollectionsBonusPacker())
            rewardInfoModels.addViewModel(rewardInfoModel)

        rewardInfoModels.invalidate()

    def __getRewardState(self, requiredCount):
        if not self.__collectionsSystem.isRewardReceived(self.__collection.collectionId, requiredCount):
            return RewardState.UNRECEIVED
        if isRewardNew(self.__collection.collectionId, requiredCount):
            return RewardState.JUSTRECEIVED
        return RewardState.RECEIVED

    def __getItemState(self, itemId):
        if not self.__collectionsSystem.isItemReceived(self.__collection.collectionId, itemId):
            return ItemState.UNRECEIVED
        if isItemNew(self.__collection.collectionId, itemId):
            return ItemState.NEW
        return ItemState.RECEIVED

    def __onSetItemReceived(self, args):
        itemId = int(args.get('itemId'))
        setItemShown(self.__collection.collectionId, itemId)
        self.__fillItems()

    def __onSetRewardReceived(self, args):
        requiredCount = int(args.get('requiredItemsCount'))
        setRewardShown(self.__collection.collectionId, requiredCount)
        self.__fillRewardsInfo()

    def __onSetProgressItemsReceived(self):
        collectionId = self.__collection.collectionId
        setShownNewItemsCount(collectionId, self.__collectionsSystem.getReceivedProgressItemCount(collectionId))
        self.__fillProgression()

    @replaceNoneKwargsModel
    def __onFinishTutorial(self, model=None):
        collectionId = self.__collection.collectionId
        setCollectionTutorialCompleted(collectionId)
        model.setIsTutorial(not isTutorialCompleted(self.__collection.collectionId))

    def __onOpenItemPreview(self, args):
        itemId = int(args.get('itemId'))
        collectionId = self.__collection.collectionId
        item = self.__collectionsSystem.getCollectionItem(collectionId, itemId)
        if item.type == 'customizationItem':
            itemType, _ = splitIntDescr(item.relatedId)
            if itemType == CustomizationType.STYLE:
                showCollectionStylePreview(item.relatedId, _getPreviewCallback(self.__appLoader, self.__collection.collectionId, self.__backCallback, self.__backBtnText), backport.text(R.strings.vehicle_preview.header.backBtn.descrLabel.collections()))
                self.__backCallback = None
                self.destroyWindow()
                return
        showCollectionItemPreviewWindow(itemId, collectionId)
        return

    @replaceNoneKwargsModel
    def __onBalanceUpdated(self, model=None):
        self.__fillItems(model=model)
        self.__fillProgression(model=model)

    def __onSettingsChanged(self):
        if not self.__collectionsSystem.isEnabled():
            showHangar()
            self.destroyWindow()


class CollectionWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, collectionId, backCallback, backBtnText, parent=None):
        super(CollectionWindow, self).__init__(WindowFlags.WINDOW, content=CollectionView(collectionId, backCallback, backBtnText), parent=parent)


def _getPreviewCallback(appLoader, collectionId, backCallback, backBtnText):

    def backToCollections(appLoader, collectionId, backCallback, backBtnText):
        containerManager = appLoader.getApp().containerManager
        stylePreview = first(containerManager.getViewByKey(ViewKey(viewAlias)) for viewAlias in (VIEW_ALIAS.STYLE_PREVIEW, VIEW_ALIAS.STYLE_PROGRESSION_PREVIEW))
        if stylePreview is not None:
            stylePreview.destroy()
        if callable(backCallback):
            backCallback()
        showCollectionWindow(collectionId, backCallback or showHangar, backBtnText)
        return

    return partial(backToCollections, appLoader, collectionId, backCallback, backBtnText)