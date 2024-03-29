# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_repr.py
from ctypes import *
import unittest
subclasses = []
for base in [c_byte, c_short, c_int, c_long, c_longlong, 
 c_ubyte, c_ushort, c_uint, 
 c_ulong, c_ulonglong, 
 c_float, c_double, c_longdouble, c_bool]:

    class X(base):
        pass


    subclasses.append(X)

class X(c_char):
    pass


class ReprTest(unittest.TestCase):

    def test_numbers(self):
        for typ in subclasses:
            base = typ.__bases__[0]
            self.assertTrue(repr(base(42)).startswith(base.__name__))
            self.assertEqual('<X object at', repr(typ(42))[:12])

    def test_char(self):
        self.assertEqual("c_char('x')", repr(c_char('x')))
        self.assertEqual('<X object at', repr(X('x'))[:12])


if __name__ == '__main__':
    unittest.main()