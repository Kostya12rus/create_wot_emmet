# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTotalPage.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.achievements.achievements_main_view import AchievementMainView, AchievementsViewCtx

class ProfileTotalPage(InjectComponentAdaptor):

    def __init__(self, *args):
        self.__userID = args[1]
        super(ProfileTotalPage, self).__init__()

    def _makeInjectView(self):
        ctx = AchievementsViewCtx(menuName=VIEW_ALIAS.PROFILE_TOTAL_PAGE, userID=self.__userID)
        self.__view = AchievementMainView(ctx)
        return self.__view

    def onSectionActivated(self):
        pass

    def onSectionDeactivated(self):
        pass