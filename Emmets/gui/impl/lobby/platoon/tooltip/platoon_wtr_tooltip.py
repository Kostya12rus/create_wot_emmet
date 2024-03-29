# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/platoon/tooltip/platoon_wtr_tooltip.py
from gui.impl.gen import R
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.platoon.common_player_data_model import CommonPlayerDataModel
from gui.impl.pub import ViewImpl

class WTRTooltip(ViewImpl):

    def __init__(self, name, clanTag, badgeID, rating):
        self.__name = name
        self.__clanTag = clanTag
        self.__badgeID = badgeID
        self.__rating = rating
        settings = ViewSettings(R.views.lobby.platoon.WTRTooltip(), model=CommonPlayerDataModel())
        super(WTRTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (model):
            model.setName(self.__name)
            model.setClanTag(self.__clanTag)
            model.setBadgeID(self.__badgeID)
            model.setRating(self.__rating)