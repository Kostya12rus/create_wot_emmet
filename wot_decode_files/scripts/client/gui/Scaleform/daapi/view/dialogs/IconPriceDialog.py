# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconPriceDialog.py
from gui.Scaleform.daapi.view.meta.IconPriceDialogMeta import IconPriceDialogMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n
from gui.shared.formatters import getItemPricesVO

class IconPriceDialog(IconPriceDialogMeta):

    def _populate(self):
        super(IconPriceDialog, self)._populate()
        self.as_setPriceLabelS(i18n.makeString(DIALOGS.REMOVECONFIRMATIONNOTREMOVABLEMONEY_MESSAGEPRICE))
        itemPrice = self._meta.getMessagePrice()
        pricesVO = getItemPricesVO(itemPrice)
        self.as_setMessagePriceS({'itemPrices': pricesVO, 'actionPrice': self._meta.getAction()})