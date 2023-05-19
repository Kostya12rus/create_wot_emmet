# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/qa_blocks.py
import BigWorld
from block import Block, Meta, InitParam, buildStrKeysValue, EDITOR_TYPE, makeResEditorData
from slot_types import SLOT_TYPE, arrayOf
from misc import ASPECT, BLOCK_MODE
from constants import IS_DEVELOPMENT

class QAMeta(Meta):

    @classmethod
    def blockCategory(cls):
        return 'QA Blocks'

    @classmethod
    def blockColor(cls):
        return 10375605

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/debug'

    @classmethod
    def mode(cls):
        return BLOCK_MODE.DEV


class TestIdentifier(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(TestIdentifier, self).__init__(*args, **kwargs)
        self._nameType, = self._getInitParams()
        if self._nameType == 'single id':
            self.inInt = self._makeDataInputSlot('test_id', SLOT_TYPE.INT)
            self.outID = self._makeDataOutputSlot('Identifier', SLOT_TYPE.ID, self._execute)
        elif self._nameType == 'array of IDs':
            self.inInt = self._makeDataInputSlot('multiple_test_ids', arrayOf(SLOT_TYPE.INT))
            self.outID = self._makeDataOutputSlot('Array of Identifiers', arrayOf(SLOT_TYPE.ID), self._execute)

    def _execute(self):
        res = self.inInt.getValue()
        self.outID.setValue(res)

    @classmethod
    def initParams(cls):
        return [
         InitParam('amount of test IDs', SLOT_TYPE.STR, buildStrKeysValue('single id', 'array of IDs'), EDITOR_TYPE.STR_KEY_SELECTOR)]


class TestSlotPyObjectToArrayVSEBlock(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(TestSlotPyObjectToArrayVSEBlock, self).__init__(*args, **kwargs)
        self._res = self._makeDataOutputSlot('res', arrayOf(SLOT_TYPE.STR), self._exec)

    def _exec(self):
        self._res.setValue(set([1, 2, 3]))


class Assert(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(Assert, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', Assert._execute)
        self._value = self._makeDataInputSlot('value', SLOT_TYPE.BOOL)
        self._msg = self._makeDataInputSlot('msg', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot('out')

    def _execute(self):
        self._out.call()


class AddTestResult(Block, QAMeta):

    def __init__(self, *args, **kwargs):
        super(AddTestResult, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self._execute)
        self._success = self._makeDataInputSlot('success', SLOT_TYPE.BOOL)
        self._msg = self._makeDataInputSlot('msg', SLOT_TYPE.STR)
        self._arena = self._makeDataInputSlot('arena', SLOT_TYPE.ARENA)
        self._out = self._makeEventOutputSlot('out')

    @property
    def _storageKey(self):
        arena = self._arena.getValue()
        runnerID = arena.ai.gameMode.arenaInfo.runnerID
        return 'runnerID_%d' % runnerID

    def _execute(self):
        if not IS_DEVELOPMENT:
            return
        BigWorld.globalData[self._storageKey]['results'].append(dict(success=self._success.getValue(), message=self._msg.getValue()))
        BigWorld.globalData[self._storageKey] = BigWorld.globalData[self._storageKey]
        self._out.call()

    def onStartScript(self):
        if not IS_DEVELOPMENT:
            return
        arena = self._arena.getValue()
        BigWorld.globalData[self._storageKey] = dict(arenaID=arena.id, results=[])

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]


class TestCase(Block):

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', TestCase._execute)
        self._name = self._makeDataInputSlot('name', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot('out')

    def _execute(self):
        self._out.call()