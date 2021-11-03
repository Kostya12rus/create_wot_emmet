# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/unit_helpers/ExtrasHandler.py
import cPickle
from debug_utils import LOG_DEBUG_DEV

class EmptyExtrasHandler(object):

    def __init__(self, unit):
        pass

    def new(self, initial=None):
        result = {}
        if initial:
            result.update(initial)
        return result

    def pack(self, extras):
        return ''

    def unpack(self, extrasStr):
        return {}

    def reset(self, extras):
        return self.new()

    def updateUnitExtras(self, extras, updateStr):
        pass


class SimpleExtrasHandler(EmptyExtrasHandler):

    def pack(self, extras):
        return cPickle.dumps(extras, -1)

    def unpack(self, extrasStr):
        return cPickle.loads(extrasStr)

    def reset(self, extras):
        return extras

    def updateUnitExtras(self, extras, updateStr):
        update = cPickle.loads(updateStr)
        extras.update(update)


class ClanBattleExtrasHandler(SimpleExtrasHandler):

    def __init__(self, unit=None):
        self._unit = unit
        from unit_helpers.MsgProcessor import ClanBattleMgrMsgProcessor
        self._processor = ClanBattleMgrMsgProcessor(unit)

    def new(self, initial=None):
        result = {'battleID': 0, 
           'scheduleTime': 0, 
           'roundStart': 0, 
           'battleResultList': [], 'isEnemyReadyForBattle': 0, 
           'clanEquipments': None, 
           'lastEquipRev': 0, 
           'localizedData': None}
        if initial:
            result.update(initial)
        return result

    def updateUnitExtras(self, extras, updateStr):
        self._processor.unpackOps(updateStr)


class SquadExtrasHandler(SimpleExtrasHandler):
    pass


class ExternalExtrasHandler(SimpleExtrasHandler):

    def new(self, initial=None):
        result = {'rev': 1}
        if initial:
            result.update(initial)
        return result