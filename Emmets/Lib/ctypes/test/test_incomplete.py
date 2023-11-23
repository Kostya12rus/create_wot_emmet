# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_incomplete.py
import unittest
from ctypes import *

class MyTestCase(unittest.TestCase):

    def test_incomplete_example(self):
        lpcell = POINTER('cell')

        class cell(Structure):
            _fields_ = [
             (
              'name', c_char_p),
             (
              'next', lpcell)]

        SetPointerType(lpcell, cell)
        c1 = cell()
        c1.name = 'foo'
        c2 = cell()
        c2.name = 'bar'
        c1.next = pointer(c2)
        c2.next = pointer(c1)
        p = c1
        result = []
        for i in range(8):
            result.append(p.name)
            p = p.next[0]

        self.assertEqual(result, ['foo', 'bar'] * 4)
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[cell]


if __name__ == '__main__':
    unittest.main()