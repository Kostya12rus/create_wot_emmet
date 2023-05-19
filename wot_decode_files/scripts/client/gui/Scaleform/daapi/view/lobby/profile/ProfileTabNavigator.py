# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTabNavigator.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection
from gui.Scaleform.daapi.view.meta.ProfileTabNavigatorMeta import ProfileTabNavigatorMeta

class ProfileTabNavigator(ProfileTabNavigatorMeta):

    def __init__(self, *args):
        ProfileTabNavigatorMeta.__init__(self)
        self.__userName = args[0]
        self.__userID = args[1]
        self.__databaseID = args[2]
        self.__navigatorOwnInitInfo = args[3]
        self.__selectedData = None
        if len(args) > 4 and args[4]:
            self.__selectedData = args[4]
        self.tabId = None
        return

    def invokeUpdate(self):
        for component in self.components.itervalues():
            if isinstance(component, ProfileSection):
                component.invokeUpdate()

    def _populate(self):
        super(ProfileTabNavigator, self)._populate()
        self.as_setInitDataS(self.__navigatorOwnInitInfo)

    def registerFlashComponent(self, component, alias, *args):
        super(ProfileTabNavigator, self).registerFlashComponent(component, alias, self.__userName, self.__userID, self.__databaseID, self.__selectedData)

    def onTabChange(self, tabId):
        self.tabId = tabId
        currentTab = self.components.get(tabId)
        if currentTab:
            currentTab.onSectionActivated()