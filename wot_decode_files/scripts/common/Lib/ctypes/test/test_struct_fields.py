# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_struct_fields.py
import unittest
from ctypes import *

class StructFieldsTestCase(unittest.TestCase):

    def test_1_A(self):

        class X(Structure):
            pass

        self.assertEqual(sizeof(X), 0)
        X._fields_ = []
        self.assertRaises(AttributeError, setattr, X, '_fields_', [])

    def test_1_B(self):

        class X(Structure):
            _fields_ = []

        self.assertRaises(AttributeError, setattr, X, '_fields_', [])

    def test_2(self):

        class X(Structure):
            pass

        X()
        self.assertRaises(AttributeError, setattr, X, '_fields_', [])

    def test_3(self):

        class X(Structure):
            pass

        class Y(Structure):
            _fields_ = [
             (
              'x', X)]

        self.assertRaises(AttributeError, setattr, X, '_fields_', [])

    def test_4(self):

        class X(Structure):
            pass

        class Y(X):
            pass

        self.assertRaises(AttributeError, setattr, X, '_fields_', [])
        Y._fields_ = []
        self.assertRaises(AttributeError, setattr, X, '_fields_', [])


if __name__ == '__main__':
    unittest.main()