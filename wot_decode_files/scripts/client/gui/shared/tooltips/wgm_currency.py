# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/wgm_currency.py
from debug_utils import LOG_ERROR
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.impl import backport
from gui.shared.formatters import text_styles
from gui.shared.money import Currency
from gui.shared.tooltips import formatters
from gui.shared.tooltips.common import DynamicBlocksTooltipData
from gui.shared.utils.requesters import wgm_balance_info_requester
from helpers import dependency
from skeletons.gui.shared import IItemsCache
_WAITING_FOR_DATA = ''
_UNKNOWN_VALUE = '-'

class WGMCurrencyTooltip(DynamicBlocksTooltipData):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx):
        super(WGMCurrencyTooltip, self).__init__(ctx, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI)
        self._setContentMargin(top=17, left=20, bottom=18, right=13)
        self._setMargins(afterBlock=0)
        self._setWidth(290)
        self.__requester = wgm_balance_info_requester.WGMBalanceInfoRequester()
        self.__data = None
        self._btnType = None
        self._hideActionBlock = None
        return

    def getWGMCurrencyValue(self, key):
        if not self.isWGMAvailable():
            return _UNKNOWN_VALUE
        else:
            if self.__data is None:
                return _WAITING_FOR_DATA
            if key in self.__data:
                return backport.getIntegralFormat(int(self.__data[key]))
            return _UNKNOWN_VALUE

    def updateData(self):
        if self.isVisible() and self.app is not None:
            self.app.updateTooltip(self.buildToolTip(btnType=self._btnType, hideActionBlock=self._hideActionBlock), self.getType())
        return

    def stopUpdates(self):
        self.__requester.clearCallbacks()
        super(WGMCurrencyTooltip, self).stopUpdates()

    def changeVisibility(self, isVisible):
        super(WGMCurrencyTooltip, self).changeVisibility(isVisible)
        if isVisible and self.isWGMAvailable():
            self.__requester.requestInfo(self.__onDataResponse)

    @classmethod
    def isWGMAvailable(cls):
        return cls.itemsCache.items.stats.mayConsumeWalletResources

    def _packBlocks(self, btnType=None, hideActionBlock=False, *args, **kwargs):
        tooltipBlocks = super(WGMCurrencyTooltip, self)._packBlocks(*args, **kwargs)
        self._btnType = btnType
        self._hideActionBlock = hideActionBlock
        if self._btnType is None:
            LOG_ERROR('WGMGoldCurrencyTooltip empty btnType!')
            return tooltipBlocks
        else:
            return formatters.packMoneyAndXpBlocks(tooltipBlocks, btnType=self._btnType, valueBlocks=self.__getValueBlocks(), alternativeData=self._getAlternativeData(), hideActionBlock=hideActionBlock)

    def _getAlternativeData(self):
        return

    def __onDataResponse(self, data):
        if self.__data is None or self.__checkDiff(self.__data, data):
            self.__data = data
            self.updateData()
        return

    @staticmethod
    def __checkDiff(d1, d2):
        s1 = frozenset(d1.itervalues())
        s2 = frozenset(d2.itervalues())
        return s1 ^ s2

    def __getValueBlocks(self):
        valueBlocks = list()
        if self._btnType == Currency.GOLD:
            valueBlocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_PURCHASEDVALUE), value=self.__getGoldString(wgm_balance_info_requester.GOLD_PURCHASED), icon=Currency.GOLD, valueWidth=84, iconYOffset=2))
            valueBlocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_EARNEDVALUE), value=self.__getGoldString(wgm_balance_info_requester.GOLD_EARNED), icon=Currency.GOLD, padding=formatters.packPadding(bottom=10), valueWidth=84, iconYOffset=2))
            valueBlocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_TOTALVALUE), value=text_styles.gold(self.__getGoldTotal()), icon=Currency.GOLD, padding=formatters.packPadding(bottom=15), valueWidth=84, iconYOffset=2))
        else:
            valueBlocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_PURCHASEDVALUE), value=self.__getCreditsString(wgm_balance_info_requester.CREDITS_PURCHASED), icon=Currency.CREDITS, valueWidth=84, iconYOffset=2))
            valueBlocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_EARNEDVALUE), value=self.__getCreditsString(wgm_balance_info_requester.CREDITS_EARNED), icon=Currency.CREDITS, padding=formatters.packPadding(bottom=10), valueWidth=84, iconYOffset=2))
            valueBlocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_TOTALVALUE), value=text_styles.credits(self.__getCreditsTotal()), icon=Currency.CREDITS, padding=formatters.packPadding(bottom=15), valueWidth=84, iconYOffset=2))
        return valueBlocks

    def __getGoldString(self, goldType):
        result = self.getWGMCurrencyValue(goldType)
        if result != _WAITING_FOR_DATA:
            return text_styles.gold(result)
        return result

    def __getGoldTotal(self):
        if self.isWGMAvailable():
            return backport.getIntegralFormat(self.itemsCache.items.stats.gold)
        return _UNKNOWN_VALUE

    def __getCreditsString(self, creditsType):
        result = self.getWGMCurrencyValue(creditsType)
        if result != _WAITING_FOR_DATA:
            return text_styles.credits(result)
        return result

    def __getCreditsTotal(self):
        if self.isWGMAvailable():
            return backport.getIntegralFormat(self.itemsCache.items.stats.credits)
        return _UNKNOWN_VALUE