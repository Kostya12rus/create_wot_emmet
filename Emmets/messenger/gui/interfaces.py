# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/interfaces.py
from messenger.gui.Scaleform import FILL_COLORS

class IGUIEntry(object):

    def init(self):
        pass

    def clear(self):
        pass

    def show(self):
        pass

    def close(self, nextScope):
        pass

    @property
    def channelsCtrl(self):
        return

    def invoke(self, method, *args, **kwargs):
        pass

    def isFocused(self):
        return False

    def handleKey(self, event):
        return False

    def addClientMessage(self, message, isCurrentPlayer=False):
        pass


class IGUIEntryDecorator(IGUIEntry):

    def getEntry(self, scope):
        pass

    def setEntry(self, scope, entry):
        pass

    def switch(self, scope):
        pass


class IControllerFactory(object):

    def init(self):
        return []

    def clear(self):
        pass

    def factory(self, entity):
        pass


class IControllersCollection(IControllerFactory):

    def getController(self, clientID):
        return

    def hasController(self, controller):
        return False

    def getControllerByCriteria(self, criteria):
        return

    def getControllersIterator(self):
        return

    def removeControllers(self):
        pass


class IEntityController(object):

    def setView(self, view):
        pass

    def removeView(self):
        pass

    def clear(self):
        pass


class IChannelController(IEntityController):

    def getChannel(self):
        return

    def join(self):
        pass

    def exit(self):
        pass

    def activate(self):
        pass

    def deactivate(self, entryClosing=False):
        pass

    def isJoined(self):
        return False

    def setHistory(self, history):
        pass

    def getHistory(self):
        return []

    def hasUnreadMessages(self):
        return len(self.getHistory()) > 0

    def setMembersDP(self, membersDP):
        pass

    def removeMembersDP(self):
        pass

    def canSendMessage(self):
        return (
         False, 'N/A')

    def sendMessage(self, message):
        pass

    def sendCommand(self, command):
        pass

    def addMessage(self, message, doFormatting=True):
        return False

    def addCommand(self, command):
        return ''

    def isEnabled(self):
        return True

    def hasUntrustedMembers(self):
        return False


class IBattleChannelView(object):

    def addController(self, ctrl):
        pass

    def removeController(self, ctrl):
        pass

    def addMessage(self, text, fillColor=FILL_COLORS.BLACK, accountDBID=0):
        pass