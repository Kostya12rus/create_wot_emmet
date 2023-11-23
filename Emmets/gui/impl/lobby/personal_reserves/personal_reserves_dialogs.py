# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_dialogs.py
from typing import TYPE_CHECKING
from uilogging.personal_reserves.loggers import BuyAndActivateDialogsLogger
from wg_async import wg_async
from adisp import adisp_async
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE
from gui.goodies.goodie_items import Booster
from gui.impl import backport
from gui.impl.dialogs.dialog_template_button import ConfirmButton, CancelButton
from gui.impl.dialogs.gf_builders import ResDialogBuilder
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent
from gui.impl.dialogs.sub_views.footer.single_price_footer import SinglePriceFooter
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencySize
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_set_view_model import IconPositionLogicEnum
from gui.impl.gen_utils import DynAccessor
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper
from gui.impl.pub.dialog_window import DialogButtons
if TYPE_CHECKING:
    from typing import Union
    from gui.impl.dialogs.dialog_template import DialogTemplateView
    from gui.shared.gui_items.gui_item_economics import ItemPrice
__all__ = ('getUpgradeBoosterDialog', 'getBuyAndActivateBoosterDialog', 'getBuyGoldDialog')
BOOSTER_IMAGE_LOOKUP = {GOODIE_RESOURCE_TYPE.XP: R.images.gui.maps.icons.quests.bonuses.s360x270.booster_xp_premium(), 
   GOODIE_RESOURCE_TYPE.CREDITS: R.images.gui.maps.icons.quests.bonuses.s360x270.booster_credits_premium(), 
   GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP: R.images.gui.maps.icons.quests.bonuses.s360x270.booster_free_xp_and_crew_xp_premium()}
UPGRADE_IMAGE_LOOKUP = {GOODIE_RESOURCE_TYPE.XP: R.images.gui.maps.icons.personal_reserves.upgrade_tank_xp(), 
   GOODIE_RESOURCE_TYPE.CREDITS: R.images.gui.maps.icons.personal_reserves.upgrade_silver_boost(), 
   GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP: R.images.gui.maps.icons.personal_reserves.upgrade_combined_xp()}

@adisp_async
@wg_async
def showDialogAndLogInteraction(dialog, dialogLogItem, callback):
    logger = BuyAndActivateDialogsLogger(dialogLogItem)
    dialog.load()
    logger.logOpenDialog()
    result = yield dialog.wait()
    buttonClicked = result.result
    logger.logButtonClick(buttonClicked)
    dialog.destroy()
    callback(buttonClicked == DialogButtons.SUBMIT)


def getUpgradeBoosterDialog(booster, previousBooster):
    builder = BuyAndActivateBoosterDialogBuilder(booster.getBuyPrice(), needsToBuy=not booster.isInAccount)
    builder.setTitle(backport.text(R.strings.personal_reserves.activation.upgradeBoosterTitle(), boosterTerm=backport.text(R.strings.personal_reserves.activation.terms.dyn(booster.boosterGuiType)()), boosterBonus=booster.getFormattedValue()))
    builder.setWarning(backport.text(R.strings.personal_reserves.activation.upgradeBoosterDescription(), previousBoosterTerm=backport.text(R.strings.personal_reserves.activation.terms.dyn(previousBooster.boosterGuiType)()), previousBoosterBonus=previousBooster.getFormattedValue()))
    builder.setIcon(mainIcon=UPGRADE_IMAGE_LOOKUP[booster.boosterType], iconPositionLogic=IconPositionLogicEnum.MOVECONTENTBELOW.value)
    return builder.build()


def getBuyAndActivateBoosterDialog(booster):
    builder = BuyAndActivateBoosterDialogBuilder(booster.getBuyPrice())
    builder.setTitle(backport.text(R.strings.personal_reserves.activation.buyAndActivateBoosterTitle(), boosterTerm=backport.text(R.strings.personal_reserves.activation.terms.dyn(booster.boosterGuiType)()), boosterBonus=booster.getFormattedValue()))
    builder.setIcon(mainIcon=BOOSTER_IMAGE_LOOKUP[booster.boosterType], iconPositionLogic=IconPositionLogicEnum.MOVECONTENTBELOW.value)
    return builder.build()


def getBuyGoldDialog(booster):
    builder = BuyGoldDialogBuilder(booster.getBuyPrice())
    builder.setTitle(backport.text(R.strings.personal_reserves.activation.buyGoldTitle(), boosterTerm=backport.text(R.strings.personal_reserves.activation.terms.dyn(booster.boosterGuiType)()), boosterBonus=booster.getFormattedValue()))
    builder.setWarning(R.strings.personal_reserves.activation.buyGoldWarning)
    builder.setIcon(mainIcon=BOOSTER_IMAGE_LOOKUP[booster.boosterType], iconPositionLogic=IconPositionLogicEnum.MOVECONTENTBELOW.value)
    return builder.build()


class BuyAndActivateBoosterDialogBuilder(ResDialogBuilder):
    __slots__ = ('boosterPrice', 'needsToBuy', 'warning')

    def __init__(self, boosterPrice, needsToBuy=True, uniqueID=None):
        super(BuyAndActivateBoosterDialogBuilder, self).__init__(uniqueID=uniqueID)
        self.boosterPrice = boosterPrice
        self.needsToBuy = needsToBuy
        self.addButton(ConfirmButton(label=self._getConfirmLabel(needsToBuy), buttonType=ButtonType.MAIN))
        self.setFocusedButtonID(DialogButtons.SUBMIT)
        self.addButton(CancelButton())
        self.setShowBalance(True)
        self.warning = None
        return

    def setWarning(self, warning):
        if isinstance(warning, int):
            warning = backport.text(warning)
        self.warning = '%(warning)' + warning

    def _extendTemplate(self, template):
        super(BuyAndActivateBoosterDialogBuilder, self)._extendTemplate(template)
        if self.boosterPrice.isDefined() and self.needsToBuy:
            template.setSubView(DefaultDialogPlaceHolders.FOOTER, SinglePriceFooter(R.strings.personal_reserves.activation.price, self.boosterPrice, CurrencySize.BIG))
        if self.warning:
            image = ImageSubstitution(R.images.gui.maps.icons.personal_reserves.warning(), 'warning', 0, 0, 0, 0)
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, SimpleTextContent(self.warning, imageSubstitutions=[image]))

    def _getConfirmLabel(self, needsToBuy):
        if needsToBuy:
            return R.strings.personal_reserves.activation.BuyAndActivateConfirm()
        return R.strings.personal_reserves.activation.ActivateConfirm()


class BuyGoldDialogBuilder(ResDialogBuilder):
    __slots__ = ('boosterPrice', 'warning')

    def __init__(self, boosterPrice, uniqueID=None):
        super(BuyGoldDialogBuilder, self).__init__(uniqueID=uniqueID)
        self.boosterPrice = boosterPrice
        self.addButton(ConfirmButton(label=R.strings.personal_reserves.activation.buyGoldConfirm(), buttonType=ButtonType.MAIN))
        self.setFocusedButtonID(DialogButtons.SUBMIT)
        self.addButton(CancelButton())
        self.setShowBalance(True)
        self.warning = None
        return

    def setWarning(self, warning):
        self.warning = warning

    def _extendTemplate(self, template):
        super(BuyGoldDialogBuilder, self)._extendTemplate(template)
        if self.boosterPrice.isDefined():
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, SinglePriceFooter(self.warning, self.boosterPrice, CurrencySize.BIG))