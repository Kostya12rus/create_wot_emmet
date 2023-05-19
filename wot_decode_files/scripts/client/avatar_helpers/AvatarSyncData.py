# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_helpers/AvatarSyncData.py
import AccountCommands

class AvatarSyncData(object):

    def __init__(self):
        self.__isSynchronized = False
        self.__subscribers = []
        self.__avatar = None
        return

    def setAvatar(self, avatar):
        self.__avatar = avatar

    def onAvatarBecomePlayer(self):
        self.__isSynchronized = self.__avatar.isSynchronized()
        if not self.__isSynchronized:
            self.__avatar._doCmdStr(AccountCommands.CMD_GET_AVATAR_SYNC, '', self.__onSyncResponse)

    def onAvatarBecomeNonPlayer(self):
        pass

    def waitForSync(self, callback):
        if self.__isSynchronized:
            callback(AccountCommands.RES_CACHE)
        if callback is not None:
            self.__subscribers.append(callback)
        return

    def __onSyncResponse(self, syncID, resultID, ext=None):
        ext = ext or {}
        self.__isSynchronized = True
        subscribers = self.__subscribers
        self.__subscribers = []
        for callback in subscribers:
            callback(resultID)