# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist_msi.py
import sys, unittest
from test.test_support import run_unittest
from distutils.tests import support

@unittest.skipUnless(sys.platform == 'win32', 'these tests require Windows')
class BDistMSITestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_minimal(self):
        from distutils.command.bdist_msi import bdist_msi
        project_dir, dist = self.create_dist()
        cmd = bdist_msi(dist)
        cmd.ensure_finalized()


def test_suite():
    return unittest.makeSuite(BDistMSITestCase)


if __name__ == '__main__':
    run_unittest(test_suite())