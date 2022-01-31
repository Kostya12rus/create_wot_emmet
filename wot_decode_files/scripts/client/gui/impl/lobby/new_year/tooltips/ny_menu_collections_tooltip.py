# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/new_year/tooltips/ny_menu_collections_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_menu_collections_tooltip_model import NyMenuCollectionsTooltipModel
from gui.impl.pub import ViewImpl
from new_year.collection_presenters import CurrentNYCollectionPresenter

class NyMenuCollectionsTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID=R.views.lobby.new_year.tooltips.NyMenuCollectionsTooltip()):
        settings = ViewSettings(layoutID)
        settings.model = NyMenuCollectionsTooltipModel()
        super(NyMenuCollectionsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NyMenuCollectionsTooltip, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(NyMenuCollectionsTooltip, self)._initialize()
        toys = str(CurrentNYCollectionPresenter.getCount())
        allToys = str(CurrentNYCollectionPresenter.getTotalCount())
        self.viewModel.setCurrentToysCount(toys)
        self.viewModel.setAllToysCount(allToys)