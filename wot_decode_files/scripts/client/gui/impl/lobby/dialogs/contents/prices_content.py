# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/contents/prices_content.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialog_prices_content_model import DialogPricesContentModel
from gui.impl.lobby.dialogs.dialog_prices_tooltip import DialogPricesTooltip
from gui.impl.pub.dialog_window import DialogContent

class DialogPricesContent(DialogContent):
    __slots__ = ('__valueMainCost', '__iconMainCost', '__labelMainCost', '__valueAdditionalCost',
                 '__iconAdditionalCost', '__labelAdditionalCost', '__totalCost',
                 '__labelTotalCost')

    def __init__(self):
        settings = ViewSettings(R.views.common.dialog_view.components.dialog_prices_content.DialogPricesContent())
        settings.model = DialogPricesContentModel()
        super(DialogPricesContent, self).__init__(settings)

    @property
    def viewModel(self):
        return super(DialogPricesContent, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == self.viewModel.getTooltipId():
            dialog = DialogPricesTooltip()
            dialog.setData(valueMainCost=self.__valueMainCost, iconMainCost=self.__iconMainCost, labelMainCost=self.__labelMainCost, valueAdditionalCost=self.__valueAdditionalCost, iconAdditionalCost=self.__iconAdditionalCost, labelAdditionalCost=self.__labelAdditionalCost, totalCost=self.__totalCost, labelTotalCost=self.__labelTotalCost)
            return dialog
        else:
            return

    def setData(self, valueMainCost, iconMainCost, labelMainCost, valueAdditionalCost, iconAdditionalCost, labelAdditionalCost, totalCost, labelTotalCost):
        self.__valueMainCost = valueMainCost
        self.__iconMainCost = iconMainCost
        self.__labelMainCost = labelMainCost
        self.__valueAdditionalCost = valueAdditionalCost
        self.__iconAdditionalCost = iconAdditionalCost
        self.__labelAdditionalCost = labelAdditionalCost
        self.__totalCost = totalCost
        self.__labelTotalCost = labelTotalCost