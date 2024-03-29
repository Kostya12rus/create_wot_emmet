# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/reusable/records.py
import operator
from ValueReplay import ValueReplay
from debug_utils import LOG_ERROR

def convertFactorToPercent(factor):
    return factor * 100


def makeReplayValueRound(value):
    return int(round(value))


class ResultRecord(object):
    __slots__ = ()

    def getRecord(self, *args):
        return 0

    def findRecord(self, criteria):
        return self.getRecord(criteria)

    def getFactor(self, *args):
        return 1.0


class RawRecords(ResultRecord):
    __slots__ = ('_records', )

    def __init__(self, records):
        super(RawRecords, self).__init__()
        self._records = records

    def getRecord(self, *names):
        result = 0
        for name in names:
            if name in self._records:
                result += self._records[name]

        return result


class ReplayRecord(ResultRecord):
    __slots__ = ('_name', '_value', '_diff')

    def __init__(self, name, value, diff):
        super(ReplayRecord, self).__init__()
        self._name = name
        self._value = value
        self._diff = diff

    def getName(self):
        return self._name

    def getRecord(self):
        return self._value

    def _getFactor(self):
        name = self._name.lower()
        if name.endswith('factor100') or name.endswith('factors100'):
            return 100
        if name.endswith('factor10') or name.endswith('factors10'):
            return 10
        return 1


class SubReplayRecord(ReplayRecord):
    __slots__ = ()

    def getRecord(self):
        return -self._value


class FactorReplayRecord(ReplayRecord):
    __slots__ = ()

    def getRecord(self):
        return self._diff

    def getFactor(self):
        return float(self._value) / self._getFactor()


class CoefficientReplayRecord(ReplayRecord):
    __slots__ = ()

    def getRecord(self):
        return self._diff


_SUPPORTED_OPS = {ValueReplay.SET: ReplayRecord, 
   ValueReplay.ADD: ReplayRecord, 
   ValueReplay.SUB: SubReplayRecord, 
   ValueReplay.MUL: FactorReplayRecord, 
   ValueReplay.FACTOR: FactorReplayRecord, 
   ValueReplay.ADDCOEFF: CoefficientReplayRecord, 
   ValueReplay.SUBCOEFF: CoefficientReplayRecord}

class ReplayRecords(ResultRecord):
    __slots__ = ('_records', )

    def __init__(self, replay, *last):
        super(ReplayRecords, self).__init__()
        self._records = {}
        currentValue = 0
        for op, (appliedName, appliedValue), (_, finalValue) in replay:
            if not isinstance(finalValue, (int, float, long)):
                LOG_ERROR('There is invalid record in the replay', op, appliedName, appliedValue, _, finalValue, replay)
                return
            self._addRecord(op, appliedName, appliedValue, finalValue - currentValue)
            currentValue = finalValue

        for name in last:
            self._addRecord(ValueReplay.SET, name, replay[name], 0)

    def getRecord(self, *names):
        result = 0
        for name in names:
            result += self._getRecord(name)

        return result

    def findRecord(self, criteria):
        result = 0
        for name, _ in self._records.iteritems():
            if name.startswith(criteria):
                result += self._getRecord(name)

        return result

    def getFactor(self, name):
        if name in self._records:
            result = self._records[name].getFactor()
        else:
            result = 1.0
        return result

    def _getRecord(self, name):
        if name in self._records:
            return self._records[name].getRecord()
        return 0

    def _addRecord(self, op, name, value, diff):
        if op in _SUPPORTED_OPS:
            clazz = _SUPPORTED_OPS[op]
            self._records[name] = clazz(name, value, diff)


class RecordsIterator(ResultRecord):
    __slots__ = ('_seq', '_indexes')

    def __init__(self, seq=None):
        super(RecordsIterator, self).__init__()
        self._seq = seq or []
        self._rebuild()

    def __iter__(self):
        self._rebuild()
        return self

    def next(self):
        while 1:
            if self._indexes:
                idx = self._indexes.pop(0)
                return idx or self
            return self._seq[idx - 1]

        raise StopIteration()

    def addRecords(self, record):
        self._seq.append(record)
        self._rebuild()

    def getRecord(self, *names):
        return self._sum('getRecord', *names)

    def findRecord(self, criteria):
        return self._sum('findRecord', criteria)

    def getFactor(self, name):
        getter = operator.methodcaller('getFactor', name)
        if self._seq:
            return max(getter(item) for item in self._seq)
        return 1

    def _rebuild(self):
        self._indexes = range(len(self._seq) + 1)

    def _sum(self, method, *names):
        getter = operator.methodcaller(method, *names)
        return sum(getter(item) for item in self._seq)