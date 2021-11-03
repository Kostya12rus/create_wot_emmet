# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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