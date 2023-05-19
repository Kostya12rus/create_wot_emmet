# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_libc.py
import unittest
from ctypes import *
import _ctypes_test
lib = CDLL(_ctypes_test.__file__)

class LibTest(unittest.TestCase):

    def test_sqrt(self):
        lib.my_sqrt.argtypes = (
         c_double,)
        lib.my_sqrt.restype = c_double
        self.assertEqual(lib.my_sqrt(4.0), 2.0)
        import math
        self.assertEqual(lib.my_sqrt(2.0), math.sqrt(2.0))

    def test_qsort(self):
        comparefunc = CFUNCTYPE(c_int, POINTER(c_char), POINTER(c_char))
        lib.my_qsort.argtypes = (c_void_p, c_size_t, c_size_t, comparefunc)
        lib.my_qsort.restype = None

        def sort(a, b):
            return cmp(a[0], b[0])

        chars = create_string_buffer('spam, spam, and spam')
        lib.my_qsort(chars, len(chars) - 1, sizeof(c_char), comparefunc(sort))
        self.assertEqual(chars.raw, '   ,,aaaadmmmnpppsss\x00')
        return


if __name__ == '__main__':
    unittest.main()