# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/collection/awards_view.py
import SoundGroups
from frameworks.wulf import ViewSettings, WindowFlags
from gui.collection.collections_helpers import composeBonuses
from gui.collection.sounds import Sounds
from gui.impl.auxiliary.collections_helper import getCollectionsBonusPacker
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.collection.awards_view_model import AwardsViewModel
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.collection.tooltips.collection_item_tooltip_view import CollectionItemTooltipView
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.event_dispatcher import showCollectionWindow, showHangar
from helpers import dependency
from skeletons.gui.game_control import ICollectionsSystemController

class AwardsView(ViewImpl):
    __slots__ = ('__collectionId', '__bonuses', '__tooltips')
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)

    def __init__(self, collectionId, bonuses):
        settings = ViewSettings(R.views.lobby.collection.AwardsView())
        settings.model = AwardsViewModel()
        self.__collectionId = collectionId
        self.__bonuses = bonuses
        self.__tooltips = {}
        super(AwardsView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(AwardsView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(AwardsView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.battle_pass.tooltips.BattlePassCoinTooltipView():
            return BattlePassCoinTooltipView()
        else:
            if contentID == R.views.lobby.collection.tooltips.CollectionItemTooltipView():
                tooltipData = self.getTooltipData(event)
                if tooltipData is not None:
                    return CollectionItemTooltipView(*tooltipData.specialArgs)
            return super(AwardsView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltips.get(tooltipId)

    def _onLoading(self, *args, **kwargs):
        super(AwardsView, self)._onLoading(*args, **kwargs)
        SoundGroups.g_instance.playSound2D(Sounds.REWARD_SCREEN.value)
        with self.viewModel.transaction() as (model):
            model.setCollectionName(self.__collectionsSystem.getCollection(self.__collectionId).name)
            self.__setAvailability(model=model)
            packBonusModelAndTooltipData(composeBonuses(self.__bonuses), model.getRewards(), self.__tooltips, getCollectionsBonusPacker())

    def _finalize(self):
        self.__tooltips = None
        super(AwardsView, self)._finalize()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onOpenCollection, self.__openCollection),
         (
          self.__collectionsSystem.onServerSettingsChanged, self.__onSettingsChanged))

    def __openCollection(self):
        showCollectionWindow(self.__collectionId)
        self.destroyWindow()

    def __onSettingsChanged(self):
        if not self.__collectionsSystem.isEnabled():
            showHangar()
            self.destroyWindow()

    @replaceNoneKwargsModel
    def __setAvailability(self, model=None):
        model.setIsDisabled(not self.__collectionsSystem.isEnabled())


class AwardsWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, collectionId, bonuses):
        super(AwardsWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=AwardsView(collectionId, bonuses))