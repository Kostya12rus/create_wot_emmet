# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/events_dispatcher.py
from debug_utils import LOG_ERROR
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shared.utils.functions import getViewName
from messenger.ext import channel_num_gen
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

def showLobbyChannelWindow(clientID):
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.LOBBY_CHANNEL_WINDOW), ctx={'clientID': clientID}), scope=EVENT_BUS_SCOPE.LOBBY)


def showLazyChannelWindow(clientID):
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.LAZY_CHANNEL_WINDOW), ctx={'clientID': clientID}), scope=EVENT_BUS_SCOPE.LOBBY)


def notifyCarousel(clientID, notify=True):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_CHANGE, {'key': 'isNotified', 
       'value': notify}), scope=EVENT_BUS_SCOPE.LOBBY)


def showConnectToSecureChannelWindow(channel):
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, getViewName(MESSENGER_VIEW_ALIAS.CONNECT_TO_SECURE_CHANNEL_WINDOW, channel.getClientID())), ctx={'channel': channel}), scope=EVENT_BUS_SCOPE.LOBBY)


def rqActivateChannel(clientID, component):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_ACTIVATE, {'component': component}), scope=EVENT_BUS_SCOPE.LOBBY)


def rqActivateLazyChannel(name, component):
    clientID = channel_num_gen.getClientID4LazyChannel(name)
    if not clientID:
        LOG_ERROR('Client ID is not found', name)
    else:
        rqActivateChannel(clientID, component)


def rqDeactivateChannel(clientID):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_DEACTIVATE), scope=EVENT_BUS_SCOPE.LOBBY)


def rqDeactivateLazyChannel(name):
    clientID = channel_num_gen.getClientID4LazyChannel(name)
    if not clientID:
        LOG_ERROR('Client ID is not found', name)
    else:
        rqDeactivateChannel(clientID)


def rqExitFromChannel(clientID):
    g_eventBus.handleEvent(events.ChannelManagementEvent(clientID, events.ChannelManagementEvent.REQUEST_TO_EXIT), scope=EVENT_BUS_SCOPE.LOBBY)


def rqExitFromLazyChannel(name):
    clientID = channel_num_gen.getClientID4LazyChannel(name)
    if not clientID:
        LOG_ERROR('Client ID is not found', name)
    else:
        rqExitFromChannel(clientID)


def setMessageFadingEnabled(isEnabled):
    g_eventBus.handleEvent(events.ChannelManagementEvent(0, events.ChannelManagementEvent.MESSAGE_FADING_ENABLED, {'isEnabled': isEnabled}), scope=EVENT_BUS_SCOPE.GLOBAL)