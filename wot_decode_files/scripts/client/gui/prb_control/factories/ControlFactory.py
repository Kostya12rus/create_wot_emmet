# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/factories/ControlFactory.py
from debug_utils import LOG_DEBUG
from gui.prb_control.items import PlayerDecorator
from gui.prb_control.settings import FUNCTIONAL_FLAG

class ControlFactory(object):

    def __del__(self):
        LOG_DEBUG('ControlFactory is deleted', self)

    def createEntry(self, ctx):
        raise NotImplementedError()

    def createEntryByAction(self, action):
        raise NotImplementedError()

    def createEntity(self, ctx):
        raise NotImplementedError()

    def createPlayerInfo(self, entity):
        return PlayerDecorator()

    def createStateEntity(self, entity):
        raise NotImplementedError()

    def createLeaveCtx(self, flags=FUNCTIONAL_FLAG.UNDEFINED, entityType=0):
        raise NotImplementedError()

    @classmethod
    def _createEntryByAction(cls, action, available):
        if action.actionName in available:
            clazz = available[action.actionName]
            result = clazz()
            result.configure(action)
            return result
        else:
            return

    @classmethod
    def _createEntryByType(cls, entryType, available):
        if entryType in available:
            clazz = available[entryType]
            return clazz()
        else:
            return

    @classmethod
    def _createEntityByType(cls, entityType, available, **kwargs):
        if entityType in available:
            clazz = available[entityType]
            return clazz(**kwargs)
        else:
            return