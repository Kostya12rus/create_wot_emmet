# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_build_py.py
import os, sys, StringIO, unittest
from distutils.command.build_py import build_py
from distutils.core import Distribution
from distutils.errors import DistutilsFileError
from distutils.tests import support
from test.test_support import run_unittest

class BuildPyTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_package_data(self):
        sources = self.mkdtemp()
        f = open(os.path.join(sources, '__init__.py'), 'w')
        try:
            f.write('# Pretend this is a package.')
        finally:
            f.close()

        f = open(os.path.join(sources, 'README.txt'), 'w')
        try:
            f.write('Info about this package')
        finally:
            f.close()

        destination = self.mkdtemp()
        dist = Distribution({'packages': ['pkg'], 'package_dir': {'pkg': sources}})
        dist.script_name = os.path.join(sources, 'setup.py')
        dist.command_obj['build'] = support.DummyCommand(force=0, build_lib=destination)
        dist.packages = ['pkg']
        dist.package_data = {'pkg': ['README.txt']}
        dist.package_dir = {'pkg': sources}
        cmd = build_py(dist)
        cmd.compile = 1
        cmd.ensure_finalized()
        self.assertEqual(cmd.package_data, dist.package_data)
        cmd.run()
        self.assertEqual(len(cmd.get_outputs()), 3)
        pkgdest = os.path.join(destination, 'pkg')
        files = os.listdir(pkgdest)
        self.assertIn('__init__.py', files)
        self.assertIn('README.txt', files)
        if sys.dont_write_bytecode:
            self.assertNotIn('__init__.pyc', files)
        else:
            self.assertIn('__init__.pyc', files)

    def test_empty_package_dir(self):
        cwd = os.getcwd()
        sources = self.mkdtemp()
        open(os.path.join(sources, '__init__.py'), 'w').close()
        testdir = os.path.join(sources, 'doc')
        os.mkdir(testdir)
        open(os.path.join(testdir, 'testfile'), 'w').close()
        os.chdir(sources)
        old_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()
        try:
            dist = Distribution({'packages': ['pkg'], 'package_dir': {'pkg': ''}, 'package_data': {'pkg': ['doc/*']}})
            dist.script_name = os.path.join(sources, 'setup.py')
            dist.script_args = ['build']
            dist.parse_command_line()
            try:
                dist.run_commands()
            except DistutilsFileError:
                self.fail("failed package_data test when package_dir is ''")

        finally:
            os.chdir(cwd)
            sys.stdout = old_stdout

    def test_dir_in_package_data(self):
        sources = self.mkdtemp()
        pkg_dir = os.path.join(sources, 'pkg')
        os.mkdir(pkg_dir)
        open(os.path.join(pkg_dir, '__init__.py'), 'w').close()
        docdir = os.path.join(pkg_dir, 'doc')
        os.mkdir(docdir)
        open(os.path.join(docdir, 'testfile'), 'w').close()
        os.mkdir(os.path.join(docdir, 'otherdir'))
        os.chdir(sources)
        dist = Distribution({'packages': ['pkg'], 'package_data': {'pkg': ['doc/*']}})
        dist.script_name = os.path.join(sources, 'setup.py')
        dist.script_args = ['build']
        dist.parse_command_line()
        try:
            dist.run_commands()
        except DistutilsFileError:
            self.fail('failed package_data when data dir includes a dir')

    def test_dont_write_bytecode(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_py(dist)
        cmd.compile = 1
        cmd.optimize = 1
        old_dont_write_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            cmd.byte_compile([])
        finally:
            sys.dont_write_bytecode = old_dont_write_bytecode

        self.assertIn('byte-compiling is disabled', self.logs[0][1])


def test_suite():
    return unittest.makeSuite(BuildPyTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())