# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/bitmask_blocks_common.py
from visual_script.block import Block, InitParam, EDITOR_TYPE, buildStrKeysValue, Meta
from visual_script.misc import errorVScript
from visual_script.slot_types import SLOT_TYPE

class BitMaskMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 4202496

    @classmethod
    def blockCategory(cls):
        return 'Bit Mask'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/automation'


class BitMaskBase(Block, BitMaskMeta):
    _MASK_TYPES = {}

    def __init__(self, *args, **kwargs):
        super(BitMaskBase, self).__init__(*args, **kwargs)
        self._flags = []
        flagsCount, bitMaskType = self._getInitParams()
        self._inFlags = {name: value for name, value in self._MASK_TYPES[bitMaskType].__dict__.iteritems() if not name.startswith('_')}
        for _ in xrange(flagsCount):
            self._addInputNode()

        self._bitMask = self._makeDataOutputSlot(bitMaskType, SLOT_TYPE.INT, self._getValue)

    def _addInputNode(self):
        self._flags.append(self._makeDataInputSlot('f' + str(len(self._flags)), SLOT_TYPE.STR, EDITOR_TYPE.ENUM_SELECTOR))
        self._flags[-1].setEditorData([ name for name in self._inFlags.iterkeys() ])

    @classmethod
    def initParams(cls):
        return [
         InitParam('Flags Count', SLOT_TYPE.INT, 1),
         InitParam('BitMask type', SLOT_TYPE.STR, buildStrKeysValue(*cls._MASK_TYPES.keys()), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def _getValue(self):
        bitMask = 0
        for f in self._flags:
            if f.hasValue():
                bitMask |= self._inFlags[f.getValue()]
            else:
                errorVScript(self, 'Not all input flags are specified')

        self._bitMask.setValue(bitMask)


class BitwiseNOT(Block, BitMaskMeta):

    def __init__(self, *args, **kwargs):
        super(BitwiseNOT, self).__init__(*args, **kwargs)
        self._a = self._makeDataInputSlot('a', SLOT_TYPE.INT)
        self._res = self._makeDataOutputSlot('res', SLOT_TYPE.INT, self._getValue)

    def _getValue(self):
        self._res.setValue(~self._a.getValue())


class BitwiseOperationBase(Block, BitMaskMeta):

    def __init__(self, *args, **kwargs):
        super(BitwiseOperationBase, self).__init__(*args, **kwargs)
        self._masks = []
        masksCount, = self._getInitParams()
        for _ in xrange(masksCount):
            self._addInputNode()

        self._addOutputNode()

    @classmethod
    def initParams(cls):
        return [InitParam('Masks Count', SLOT_TYPE.INT, 1)]

    @property
    def _maskValues(self):
        return [ long(m.getValue()) for m in self._masks ]

    def _addInputNode(self):
        self._masks.append(self._makeDataInputSlot('m' + str(len(self._masks)), SLOT_TYPE.INT))

    def _addOutputNode(self):
        self._res = self._makeDataOutputSlot('res', SLOT_TYPE.INT, self._getValue)

    def _getValue(self):
        raise NotImplementedError


class BitwiseAND(BitwiseOperationBase):

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(reduce(long.__and__, masks[1:], masks[0]))


class BitwiseOR(BitwiseOperationBase):

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(reduce(long.__or__, masks[1:], masks[0]))


class BitwiseXOR(BitwiseOperationBase):

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(reduce(long.__xor__, masks[1:], masks[0]))


class BitwiseEQUAL(BitwiseOperationBase):

    def _addOutputNode(self):
        self._res = self._makeDataOutputSlot('res', SLOT_TYPE.BOOL, self._getValue)

    def _getValue(self):
        masks = self._maskValues
        self._res.setValue(all(m == masks[0] for m in masks[1:]))