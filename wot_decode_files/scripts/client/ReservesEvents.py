# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ReservesEvents.py
import Event

class ReservesEvents(object):

    def __init__(self):
        self.onShowPanel = Event.Event()
        self.onSelectedReserve = Event.Event()
        self.onUpdate = Event.Event()
        self.onShownPanel = Event.Event()
        self.hidePanel = Event.Event()
        self.showPanel = Event.Event()


randomReservesEvents = ReservesEvents()