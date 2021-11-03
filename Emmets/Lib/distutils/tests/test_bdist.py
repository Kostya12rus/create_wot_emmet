# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist.py
import os, unittest
from test.test_support import run_unittest
from distutils.command.bdist import bdist
from distutils.tests import support

class BuildTestCase(support.TempdirManager, unittest.TestCase):

    def test_formats(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.formats = ['msi']
        cmd.ensure_finalized()
        self.assertEqual(cmd.formats, ['msi'])
        formats = [
         'bztar', 'gztar', 'msi', 'rpm', 'tar',
         'wininst', 'zip', 'ztar']
        found = sorted(cmd.format_command)
        self.assertEqual(found, formats)

    def test_skip_build(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.skip_build = 1
        cmd.ensure_finalized()
        dist.command_obj['bdist'] = cmd
        names = [
         'bdist_dumb', 'bdist_wininst']
        if os.name == 'nt':
            names.append('bdist_msi')
        for name in names:
            subcmd = cmd.get_finalized_command(name)
            self.assertTrue(subcmd.skip_build, '%s should take --skip-build from bdist' % name)


def test_suite():
    return unittest.makeSuite(BuildTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())