# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_objects.py
import unittest, doctest, sys, ctypes.test.test_objects

class TestCase(unittest.TestCase):

    def test(self):
        failures, tests = doctest.testmod(ctypes.test.test_objects)
        self.assertFalse(failures, 'doctests failed, see output above')


if __name__ == '__main__':
    doctest.testmod(ctypes.test.test_objects)