# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_util.py
import sys, unittest
from test.test_support import run_unittest
from distutils.errors import DistutilsByteCompileError
from distutils.util import byte_compile, grok_environment_error

class UtilTestCase(unittest.TestCase):

    def test_dont_write_bytecode(self):
        old_dont_write_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            self.assertRaises(DistutilsByteCompileError, byte_compile, [])
        finally:
            sys.dont_write_bytecode = old_dont_write_bytecode

    def test_grok_environment_error(self):
        exc = IOError('Unable to find batch file')
        msg = grok_environment_error(exc)
        self.assertEqual(msg, 'error: Unable to find batch file')


def test_suite():
    return unittest.makeSuite(UtilTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())