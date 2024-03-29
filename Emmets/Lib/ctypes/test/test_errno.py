# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_errno.py
import unittest, os, errno
from ctypes import *
from ctypes.util import find_library
from test import test_support
try:
    import threading
except ImportError:
    threading = None

class Test(unittest.TestCase):

    def test_open(self):
        libc_name = find_library('c')
        if libc_name is None:
            raise unittest.SkipTest('Unable to find C library')
        libc = CDLL(libc_name, use_errno=True)
        if os.name == 'nt':
            libc_open = libc._open
        else:
            libc_open = libc.open
        libc_open.argtypes = (c_char_p, c_int)
        self.assertEqual(libc_open('', 0), -1)
        self.assertEqual(get_errno(), errno.ENOENT)
        self.assertEqual(set_errno(32), errno.ENOENT)
        self.assertEqual(get_errno(), 32)
        if threading:

            def _worker():
                set_errno(0)
                libc = CDLL(libc_name, use_errno=False)
                if os.name == 'nt':
                    libc_open = libc._open
                else:
                    libc_open = libc.open
                libc_open.argtypes = (
                 c_char_p, c_int)
                self.assertEqual(libc_open('', 0), -1)
                self.assertEqual(get_errno(), 0)

            t = threading.Thread(target=_worker)
            t.start()
            t.join()
            self.assertEqual(get_errno(), 32)
            set_errno(0)
        return

    @unittest.skipUnless(os.name == 'nt', 'Test specific to Windows')
    def test_GetLastError(self):
        dll = WinDLL('kernel32', use_last_error=True)
        GetModuleHandle = dll.GetModuleHandleA
        GetModuleHandle.argtypes = [c_wchar_p]
        self.assertEqual(0, GetModuleHandle('foo'))
        self.assertEqual(get_last_error(), 126)
        self.assertEqual(set_last_error(32), 126)
        self.assertEqual(get_last_error(), 32)

        def _worker():
            set_last_error(0)
            dll = WinDLL('kernel32', use_last_error=False)
            GetModuleHandle = dll.GetModuleHandleW
            GetModuleHandle.argtypes = [c_wchar_p]
            GetModuleHandle('bar')
            self.assertEqual(get_last_error(), 0)

        t = threading.Thread(target=_worker)
        t.start()
        t.join()
        self.assertEqual(get_last_error(), 32)
        set_last_error(0)


if __name__ == '__main__':
    unittest.main()