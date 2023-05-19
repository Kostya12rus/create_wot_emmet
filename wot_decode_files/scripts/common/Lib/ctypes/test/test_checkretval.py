# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_checkretval.py
import unittest
from ctypes import *
from ctypes.test import need_symbol

class CHECKED(c_int):

    def _check_retval_(value):
        return str(value.value)

    _check_retval_ = staticmethod(_check_retval_)


class Test(unittest.TestCase):

    def test_checkretval(self):
        import _ctypes_test
        dll = CDLL(_ctypes_test.__file__)
        self.assertEqual(42, dll._testfunc_p_p(42))
        dll._testfunc_p_p.restype = CHECKED
        self.assertEqual('42', dll._testfunc_p_p(42))
        dll._testfunc_p_p.restype = None
        self.assertEqual(None, dll._testfunc_p_p(42))
        del dll._testfunc_p_p.restype
        self.assertEqual(42, dll._testfunc_p_p(42))
        return

    @need_symbol('oledll')
    def test_oledll(self):
        self.assertRaises(WindowsError, oledll.oleaut32.CreateTypeLib2, 0, None, None)
        return


if __name__ == '__main__':
    unittest.main()