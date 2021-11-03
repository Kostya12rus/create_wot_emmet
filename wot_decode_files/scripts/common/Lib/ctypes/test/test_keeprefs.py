# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_keeprefs.py
from ctypes import *
import unittest

class SimpleTestCase(unittest.TestCase):

    def test_cint(self):
        x = c_int()
        self.assertEqual(x._objects, None)
        x.value = 42
        self.assertEqual(x._objects, None)
        x = c_int(99)
        self.assertEqual(x._objects, None)
        return

    def test_ccharp(self):
        x = c_char_p()
        self.assertEqual(x._objects, None)
        x.value = 'abc'
        self.assertEqual(x._objects, 'abc')
        x = c_char_p('spam')
        self.assertEqual(x._objects, 'spam')
        return


class StructureTestCase(unittest.TestCase):

    def test_cint_struct(self):

        class X(Structure):
            _fields_ = [
             (
              'a', c_int),
             (
              'b', c_int)]

        x = X()
        self.assertEqual(x._objects, None)
        x.a = 42
        x.b = 99
        self.assertEqual(x._objects, None)
        return

    def test_ccharp_struct(self):

        class X(Structure):
            _fields_ = [
             (
              'a', c_char_p),
             (
              'b', c_char_p)]

        x = X()
        self.assertEqual(x._objects, None)
        x.a = 'spam'
        x.b = 'foo'
        self.assertEqual(x._objects, {'0': 'spam', '1': 'foo'})
        return

    def test_struct_struct(self):

        class POINT(Structure):
            _fields_ = [
             (
              'x', c_int), ('y', c_int)]

        class RECT(Structure):
            _fields_ = [
             (
              'ul', POINT), ('lr', POINT)]

        r = RECT()
        r.ul.x = 0
        r.ul.y = 1
        r.lr.x = 2
        r.lr.y = 3
        self.assertEqual(r._objects, None)
        r = RECT()
        pt = POINT(1, 2)
        r.ul = pt
        self.assertEqual(r._objects, {'0': {}})
        r.ul.x = 22
        r.ul.y = 44
        self.assertEqual(r._objects, {'0': {}})
        r.lr = POINT()
        self.assertEqual(r._objects, {'0': {}, '1': {}})
        return


class ArrayTestCase(unittest.TestCase):

    def test_cint_array(self):
        INTARR = c_int * 3
        ia = INTARR()
        self.assertEqual(ia._objects, None)
        ia[0] = 1
        ia[1] = 2
        ia[2] = 3
        self.assertEqual(ia._objects, None)

        class X(Structure):
            _fields_ = [
             (
              'x', c_int),
             (
              'a', INTARR)]

        x = X()
        x.x = 1000
        x.a[0] = 42
        x.a[1] = 96
        self.assertEqual(x._objects, None)
        x.a = ia
        self.assertEqual(x._objects, {'1': {}})
        return


class PointerTestCase(unittest.TestCase):

    def test_p_cint(self):
        i = c_int(42)
        x = pointer(i)
        self.assertEqual(x._objects, {'1': i})


class DeletePointerTestCase(unittest.TestCase):

    def X_test(self):

        class X(Structure):
            _fields_ = [
             (
              'p', POINTER(c_char_p))]

        x = X()
        i = c_char_p('abc def')
        from sys import getrefcount as grc
        print '2?', grc(i)
        x.p = pointer(i)
        print '3?', grc(i)
        for i in range(320):
            c_int(99)
            x.p[0]

        print x.p[0]
        import gc
        gc.collect()
        for i in range(320):
            c_int(99)
            x.p[0]

        print x.p[0]
        print x.p.contents
        x.p[0] = 'spam spam'
        print '+' * 42
        print x._objects


class PointerToStructure(unittest.TestCase):

    def test(self):

        class POINT(Structure):
            _fields_ = [
             (
              'x', c_int), ('y', c_int)]

        class RECT(Structure):
            _fields_ = [
             (
              'a', POINTER(POINT)),
             (
              'b', POINTER(POINT))]

        r = RECT()
        p1 = POINT(1, 2)
        r.a = pointer(p1)
        r.b = pointer(p1)
        r.a[0].x = 42
        r.a[0].y = 99
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[POINT]


if __name__ == '__main__':
    unittest.main()