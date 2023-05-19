# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/_endian.py
import sys
from ctypes import *
_array_type = type(Array)

def _other_endian(typ):
    if hasattr(typ, _OTHER_ENDIAN):
        return getattr(typ, _OTHER_ENDIAN)
    if isinstance(typ, _array_type):
        return _other_endian(typ._type_) * typ._length_
    if issubclass(typ, Structure):
        return typ
    raise TypeError('This type does not support other endian: %s' % typ)


class _swapped_meta(type(Structure)):

    def __setattr__(self, attrname, value):
        if attrname == '_fields_':
            fields = []
            for desc in value:
                name = desc[0]
                typ = desc[1]
                rest = desc[2:]
                fields.append((name, _other_endian(typ)) + rest)

            value = fields
        super(_swapped_meta, self).__setattr__(attrname, value)


if sys.byteorder == 'little':
    _OTHER_ENDIAN = '__ctype_be__'
    LittleEndianStructure = Structure

    class BigEndianStructure(Structure):
        __metaclass__ = _swapped_meta
        _swappedbytes_ = None


elif sys.byteorder == 'big':
    _OTHER_ENDIAN = '__ctype_le__'
    BigEndianStructure = Structure

    class LittleEndianStructure(Structure):
        __metaclass__ = _swapped_meta
        _swappedbytes_ = None


else:
    raise RuntimeError('Invalid byteorder')