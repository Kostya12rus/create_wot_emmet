# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_post_progression/formatters/ext_currency.py
from gui.impl import backport
from gui.shared.formatters import text_styles
from gui.shared.formatters.currency import getBWFormatter, getStyle
from gui.veh_post_progression.models.ext_money import ExtendedCurrency
_EXTENDED_CURRENCY_TO_BW_FORMATTER = {ExtendedCurrency.VEH_XP: backport.getIntegralFormat, 
   ExtendedCurrency.XP: backport.getIntegralFormat, 
   ExtendedCurrency.FREE_XP: backport.getIntegralFormat}
_EXTENDED_CURRENCY_TO_TEXT_STYLE = {ExtendedCurrency.VEH_XP: text_styles.expText, 
   ExtendedCurrency.XP: text_styles.expText, 
   ExtendedCurrency.FREE_XP: text_styles.expText}

def formatExtendedCurrencyValue(currency, value, useStyle=True):
    if currency in _EXTENDED_CURRENCY_TO_BW_FORMATTER:
        bwFormatter = _EXTENDED_CURRENCY_TO_BW_FORMATTER[currency]
    else:
        bwFormatter = getBWFormatter(currency)
    fValue = bwFormatter(value)
    if useStyle:
        if currency in _EXTENDED_CURRENCY_TO_TEXT_STYLE:
            style = _EXTENDED_CURRENCY_TO_TEXT_STYLE[currency]
        else:
            style = getStyle(currency)
        fValue = style(fValue)
    return fValue