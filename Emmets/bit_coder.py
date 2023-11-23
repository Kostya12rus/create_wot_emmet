# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/bit_coder.py


class BitCoder:

    def __init__(self, *args):
        self.__dimension = sum(args)
        self.__fieldDescriptor = tuple(args)
        self.__fieldDescriptorLen = len(self.__fieldDescriptor)

    @staticmethod
    def mask(bits):
        return 2 ** bits - 1

    def extract(self, bitField):
        res = [
         0] * self.__fieldDescriptorLen
        shift = self.__dimension
        mask = self.mask
        for i, v in enumerate(self.__fieldDescriptor):
            shift -= v
            res[i] = bitField >> shift & mask(v)

        return tuple(res)

    def emplace(self, *fields):
        res = 0
        shift = self.__dimension
        fieldDescriptor = self.__fieldDescriptor
        mask = self.mask
        for i, f in enumerate(fields):
            bitCount = fieldDescriptor[i]
            shift -= bitCount
            res |= (f & mask(bitCount)) << shift

        return res

    def checkFit(self, fieldIndex, value):
        return value <= self.mask(self.__fieldDescriptor[fieldIndex])