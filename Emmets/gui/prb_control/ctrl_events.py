# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/ctrl_events.py
import Event

class _PrbCtrlEvents(object):
    __slots__ = ('__eManager', 'onLegacyIntroModeJoined', 'onLegacyIntroModeLeft',
                 'onUnitIntroModeLeft', 'onLegacyInited', 'onUnitIntroModeJoined',
                 'onUnitBrowserModeLeft', 'onUnitCreationFailure', 'onPreQueueJoined',
                 'onPreQueueJoinFailure', 'onPreQueueLeft', 'onVehicleClientStateChanged')

    def __init__(self):
        super(_PrbCtrlEvents, self).__init__()
        self.__eManager = Event.EventManager()
        self.onLegacyIntroModeJoined = Event.Event(self.__eManager)
        self.onLegacyIntroModeLeft = Event.Event(self.__eManager)
        self.onLegacyInited = Event.Event(self.__eManager)
        self.onUnitIntroModeJoined = Event.Event(self.__eManager)
        self.onUnitIntroModeLeft = Event.Event(self.__eManager)
        self.onUnitBrowserModeLeft = Event.Event(self.__eManager)
        self.onPreQueueJoined = Event.Event(self.__eManager)
        self.onPreQueueJoinFailure = Event.Event(self.__eManager)
        self.onUnitCreationFailure = Event.Event(self.__eManager)
        self.onPreQueueLeft = Event.Event(self.__eManager)
        self.onVehicleClientStateChanged = Event.Event(self.__eManager)

    def clear(self):
        self.__eManager.clear()


g_prbCtrlEvents = _PrbCtrlEvents()