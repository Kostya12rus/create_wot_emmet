# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_refcounts.py
import unittest, ctypes, gc
MyCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
OtherCallback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_ulonglong)
import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)

class RefcountTestCase(unittest.TestCase):

    def test_1(self):
        from sys import getrefcount as grc
        f = dll._testfunc_callback_i_if
        f.restype = ctypes.c_int
        f.argtypes = [ctypes.c_int, MyCallback]

        def callback(value):
            return value

        self.assertEqual(grc(callback), 2)
        cb = MyCallback(callback)
        self.assertGreater(grc(callback), 2)
        result = f(-10, cb)
        self.assertEqual(result, -18)
        cb = None
        gc.collect()
        self.assertEqual(grc(callback), 2)
        return

    def test_refcount(self):
        from sys import getrefcount as grc

        def func(*args):
            pass

        self.assertEqual(grc(func), 2)
        f = OtherCallback(func)
        self.assertGreater(grc(func), 2)
        del f
        self.assertGreaterEqual(grc(func), 2)
        gc.collect()
        self.assertEqual(grc(func), 2)

        class X(ctypes.Structure):
            _fields_ = [
             (
              'a', OtherCallback)]

        x = X()
        x.a = OtherCallback(func)
        self.assertGreater(grc(func), 2)
        del x
        self.assertGreaterEqual(grc(func), 2)
        gc.collect()
        self.assertEqual(grc(func), 2)
        f = OtherCallback(func)
        self.assertGreater(grc(func), 2)
        f.cycle = f
        del f
        gc.collect()
        self.assertEqual(grc(func), 2)


class AnotherLeak(unittest.TestCase):

    def test_callback(self):
        import sys
        proto = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

        def func(a, b):
            return a * b * 2

        f = proto(func)
        a = sys.getrefcount(ctypes.c_int)
        f(1, 2)
        self.assertEqual(sys.getrefcount(ctypes.c_int), a)


if __name__ == '__main__':
    unittest.main()