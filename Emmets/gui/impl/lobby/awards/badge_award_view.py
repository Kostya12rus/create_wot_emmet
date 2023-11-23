# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/awards/badge_award_view.py
import typing
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.awards.badge_award_view_model import BadgeAwardViewModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.badge import Badge

class BadgeAwardView(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.awards.BadgeAwardView())
        settings.model = BadgeAwardViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(BadgeAwardView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BadgeAwardView, self).getViewModel()

    def _onLoading(self, badge):
        with self.viewModel.transaction() as (model):
            model.setBadgeId(badge.badgeID)


class BadgeAwardViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, badge, parent=None):
        super(BadgeAwardViewWindow, self).__init__(content=BadgeAwardView(badge), parent=parent)