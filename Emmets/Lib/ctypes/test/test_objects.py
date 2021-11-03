# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_objects.py
import unittest, doctest, sys, ctypes.test.test_objects

class TestCase(unittest.TestCase):
    if sys.hexversion > 33816576:

        def test(self):
            doctest.testmod(ctypes.test.test_objects)


if __name__ == '__main__':
    if sys.hexversion > 33816576:
        doctest.testmod(ctypes.test.test_objects)