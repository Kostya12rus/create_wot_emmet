# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_install_headers.py
import sys, os, unittest, getpass
from distutils.command.install_headers import install_headers
from distutils.tests import support
from test.test_support import run_unittest

class InstallHeadersTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def test_simple_run(self):
        header_list = self.mkdtemp()
        header1 = os.path.join(header_list, 'header1')
        header2 = os.path.join(header_list, 'header2')
        self.write_file(header1)
        self.write_file(header2)
        headers = [header1, header2]
        pkg_dir, dist = self.create_dist(headers=headers)
        cmd = install_headers(dist)
        self.assertEqual(cmd.get_inputs(), headers)
        cmd.install_dir = os.path.join(pkg_dir, 'inst')
        cmd.ensure_finalized()
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 2)


def test_suite():
    return unittest.makeSuite(InstallHeadersTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())