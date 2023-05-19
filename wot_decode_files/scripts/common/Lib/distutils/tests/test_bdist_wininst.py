# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist_wininst.py
import unittest
from test.test_support import run_unittest
from distutils.command.bdist_wininst import bdist_wininst
from distutils.tests import support

class BuildWinInstTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_get_exe_bytes(self):
        pkg_pth, dist = self.create_dist()
        cmd = bdist_wininst(dist)
        cmd.ensure_finalized()
        exe_file = cmd.get_exe_bytes()
        self.assertGreater(len(exe_file), 10)


def test_suite():
    return unittest.makeSuite(BuildWinInstTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())