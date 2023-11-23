# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/events_handler.py
from inspect import isfunction, ismethod, getmembers
from metaclass import Metaclass
from typing import Callable
from operator import attrgetter

def eventHandler(func):
    func.isEventHandler = True
    return func


def _isEventHandler(func):
    return getattr(func, 'isEventHandler', False)


def _isMethodEventHandler(method):
    return ismethod(method) and _isEventHandler(method)


def _isFunctionEventHandler(function):
    return isfunction(function) and _isEventHandler(function)


def _getEventHandlers(handler):
    try:
        eventHandlers = handler.__eventHandlers__
    except AttributeError:
        eventHandlers = getmembers(type(handler), _isMethodEventHandler)

    return [ (name, method.__get__(handler)) for name, method in eventHandlers ]


def subscribeToEvents(handler, events):
    result = False
    if events is not None:
        for name, method in _getEventHandlers(handler):
            event = getattr(events, name)
            event += method
            result = True

    return result


def unsubscribeFromEvents(handler, events):
    result = False
    if events is not None:
        for name, method in _getEventHandlers(handler):
            event = getattr(events, name)
            event -= method
            result = True

    return result


class EventsHandler(object):
    __metaclass__ = Metaclass

    @classmethod
    def __init_subclass__(cls, _, bases, attributes):
        cls.__eventHandlers__ = getmembers(cls, _isMethodEventHandler)

    def _subscribeToEvents(self, events):
        return subscribeToEvents(self, events)

    def _unsubscribeFromEvents(self, events):
        return unsubscribeFromEvents(self, events)


class EventsQuery(object):
    EVENTS_PROPERTY_NAME = None
    __metaclass__ = Metaclass

    @classmethod
    def __init_subclass__(cls, _, bases, attributes):
        if cls.EVENTS_PROPERTY_NAME:
            cls.__eventsQuery__ = attrgetter(cls.EVENTS_PROPERTY_NAME)
        else:
            cls.__eventsQuery__ = lambda *args: None

    def _getEvents(self, object):
        try:
            return self.__eventsQuery__(object)
        except AttributeError:
            return

        return