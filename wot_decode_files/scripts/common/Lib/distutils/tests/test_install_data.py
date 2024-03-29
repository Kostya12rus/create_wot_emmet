# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_install_data.py
import sys, os, unittest, getpass
from distutils.command.install_data import install_data
from distutils.tests import support
from test.test_support import run_unittest

class InstallDataTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def test_simple_run(self):
        pkg_dir, dist = self.create_dist()
        cmd = install_data(dist)
        cmd.install_dir = inst = os.path.join(pkg_dir, 'inst')
        one = os.path.join(pkg_dir, 'one')
        self.write_file(one, 'xxx')
        inst2 = os.path.join(pkg_dir, 'inst2')
        two = os.path.join(pkg_dir, 'two')
        self.write_file(two, 'xxx')
        cmd.data_files = [
         one, (inst2, [two])]
        self.assertEqual(cmd.get_inputs(), [one, (inst2, [two])])
        cmd.ensure_finalized()
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 2)
        rtwo = os.path.split(two)[-1]
        self.assertTrue(os.path.exists(os.path.join(inst2, rtwo)))
        rone = os.path.split(one)[-1]
        self.assertTrue(os.path.exists(os.path.join(inst, rone)))
        cmd.outfiles = []
        cmd.warn_dir = 1
        cmd.ensure_finalized()
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 2)
        self.assertTrue(os.path.exists(os.path.join(inst2, rtwo)))
        self.assertTrue(os.path.exists(os.path.join(inst, rone)))
        cmd.outfiles = []
        cmd.root = os.path.join(pkg_dir, 'root')
        inst3 = os.path.join(cmd.install_dir, 'inst3')
        inst4 = os.path.join(pkg_dir, 'inst4')
        three = os.path.join(cmd.install_dir, 'three')
        self.write_file(three, 'xx')
        cmd.data_files = [one, (inst2, [two]),
         (
          'inst3', [three]),
         (
          inst4, [])]
        cmd.ensure_finalized()
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 4)
        self.assertTrue(os.path.exists(os.path.join(inst2, rtwo)))
        self.assertTrue(os.path.exists(os.path.join(inst, rone)))


def test_suite():
    return unittest.makeSuite(InstallDataTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())