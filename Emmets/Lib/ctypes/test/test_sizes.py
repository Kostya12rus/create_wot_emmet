# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_sizes.py
from ctypes import *
import sys, unittest

class SizesTestCase(unittest.TestCase):

    def test_8(self):
        self.assertEqual(1, sizeof(c_int8))
        self.assertEqual(1, sizeof(c_uint8))

    def test_16(self):
        self.assertEqual(2, sizeof(c_int16))
        self.assertEqual(2, sizeof(c_uint16))

    def test_32(self):
        self.assertEqual(4, sizeof(c_int32))
        self.assertEqual(4, sizeof(c_uint32))

    def test_64(self):
        self.assertEqual(8, sizeof(c_int64))
        self.assertEqual(8, sizeof(c_uint64))

    def test_size_t(self):
        self.assertEqual(sizeof(c_void_p), sizeof(c_size_t))

    def test_ssize_t(self):
        self.assertEqual(sizeof(c_void_p), sizeof(c_ssize_t))


if __name__ == '__main__':
    unittest.main()