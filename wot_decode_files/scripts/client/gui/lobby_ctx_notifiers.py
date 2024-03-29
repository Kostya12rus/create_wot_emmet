# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lobby_ctx_notifiers.py
from collections import namedtuple
from gui import SystemMessages
from gui.impl import backport
from gui.shared.notifications import NotificationPriorityLevel
NotifySysMessages = namedtuple('NotifySysMessages', 'resID, priority, type')
NotifySysMessages.__new__.__defaults__ = (
 None, NotificationPriorityLevel.MEDIUM, SystemMessages.SM_TYPE.Information)

class BaseNotifier(object):
    __slots__ = ()

    def getPath(self):
        raise NotImplementedError


class SimpleSysMessageNotifier(BaseNotifier):
    __slots__ = ('__states', '__path')

    def __init__(self, path, states):
        self.__path = path
        self.__states = states

    def __call__(self, nextValue, currentValue):
        if (
         currentValue, nextValue) in self.__states:
            msg = self.__states[(currentValue, nextValue)]
            SystemMessages.pushMessage(backport.text(msg.resID), priority=msg.priority, type=msg.type)

    def getPath(self):
        return self.__path