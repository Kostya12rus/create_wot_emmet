# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_clean.py
import sys, os, unittest, getpass
from distutils.command.clean import clean
from distutils.tests import support
from test.test_support import run_unittest

class cleanTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_simple_run(self):
        pkg_dir, dist = self.create_dist()
        cmd = clean(dist)
        dirs = [ (d, os.path.join(pkg_dir, d)) for d in ('build_temp', 'build_lib',
                                                         'bdist_base', 'build_scripts',
                                                         'build_base')
               ]
        for name, path in dirs:
            os.mkdir(path)
            setattr(cmd, name, path)
            if name == 'build_base':
                continue
            for f in ('one', 'two', 'three'):
                self.write_file(os.path.join(path, f))

        cmd.all = 1
        cmd.ensure_finalized()
        cmd.run()
        for name, path in dirs:
            self.assertFalse(os.path.exists(path), '%s was not removed' % path)

        cmd.all = 1
        cmd.ensure_finalized()
        cmd.run()


def test_suite():
    return unittest.makeSuite(cleanTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())