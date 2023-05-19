# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/dialogs/dialog_prices_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.windows.dialog_prices_tooltip_model import DialogPricesTooltipModel
from gui.impl.pub import ViewImpl

class DialogPricesTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.common.dialog_view.components.dialog_prices_tooltip.DialogPricesTooltip())
        settings.model = DialogPricesTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(DialogPricesTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(DialogPricesTooltip, self).getViewModel()

    def setData(self, valueMainCost, iconMainCost, labelMainCost, valueAdditionalCost, iconAdditionalCost, labelAdditionalCost, totalCost, labelTotalCost):
        with self.viewModel.transaction() as (model):
            model.setValueMainCost(valueMainCost)
            model.setIconMainCost(iconMainCost)
            model.setLabelMainCost(labelMainCost)
            model.setValueAdditionalCost(valueAdditionalCost)
            model.setIconAdditionalCost(iconAdditionalCost)
            model.setLabelAdditionalCost(labelAdditionalCost)
            model.setTotalCost(self.gui.systemLocale.getNumberFormat(totalCost))
            model.setLabelTotalCost(labelTotalCost)