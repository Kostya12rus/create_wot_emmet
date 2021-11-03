# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/bit_coder.py


class BitCoder:

    def __init__(self, *args):
        self.dimension = sum(args)
        self.fieldDescriptor = tuple(args)

    @staticmethod
    def mask(bits):
        return 2 ** bits - 1

    def extract(self, bitField):
        res = [
         0] * len(self.fieldDescriptor)
        shift = self.dimension
        for i, v in enumerate(self.fieldDescriptor):
            shift -= v
            res[i] = bitField >> shift & self.mask(v)

        return tuple(res)

    def emplace(self, *fields):
        res = 0
        shift = self.dimension
        for i, f in enumerate(fields):
            bitCount = self.fieldDescriptor[i]
            shift -= bitCount
            res |= (f & self.mask(bitCount)) << shift

        return res

    def checkFit(self, fieldIndex, value):
        return value <= self.mask(self.fieldDescriptor[fieldIndex])