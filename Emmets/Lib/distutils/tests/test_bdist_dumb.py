# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist_dumb.py
import os, sys, zipfile, unittest
from test.test_support import run_unittest
try:
    import zlib
except ImportError:
    zlib = None

from distutils.core import Distribution
from distutils.command.bdist_dumb import bdist_dumb
from distutils.tests import support
SETUP_PY = "from distutils.core import setup\nimport foo\n\nsetup(name='foo', version='0.1', py_modules=['foo'],\n      url='xxx', author='xxx', author_email='xxx')\n\n"

class BuildDumbTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def setUp(self):
        super(BuildDumbTestCase, self).setUp()
        self.old_location = os.getcwd()
        self.old_sys_argv = (sys.argv, sys.argv[:])

    def tearDown(self):
        os.chdir(self.old_location)
        sys.argv = self.old_sys_argv[0]
        sys.argv[:] = self.old_sys_argv[1]
        super(BuildDumbTestCase, self).tearDown()

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_simple_built(self):
        tmp_dir = self.mkdtemp()
        pkg_dir = os.path.join(tmp_dir, 'foo')
        os.mkdir(pkg_dir)
        self.write_file((pkg_dir, 'setup.py'), SETUP_PY)
        self.write_file((pkg_dir, 'foo.py'), '#')
        self.write_file((pkg_dir, 'MANIFEST.in'), 'include foo.py')
        self.write_file((pkg_dir, 'README'), '')
        dist = Distribution({'name': 'foo', 'version': '0.1', 'py_modules': [
                        'foo'], 
           'url': 'xxx', 
           'author': 'xxx', 'author_email': 'xxx'})
        dist.script_name = 'setup.py'
        os.chdir(pkg_dir)
        sys.argv = [
         'setup.py']
        cmd = bdist_dumb(dist)
        cmd.format = 'zip'
        cmd.ensure_finalized()
        cmd.run()
        dist_created = os.listdir(os.path.join(pkg_dir, 'dist'))
        base = '%s.%s.zip' % (dist.get_fullname(), cmd.plat_name)
        if os.name == 'os2':
            base = base.replace(':', '-')
        self.assertEqual(dist_created, [base])
        fp = zipfile.ZipFile(os.path.join('dist', base))
        try:
            contents = fp.namelist()
        finally:
            fp.close()

        contents = sorted(filter(None, map(os.path.basename, contents)))
        wanted = ['foo-0.1-py%s.%s.egg-info' % sys.version_info[:2], 'foo.py']
        if not sys.dont_write_bytecode:
            wanted.append('foo.pyc')
        self.assertEqual(contents, sorted(wanted))
        return

    def test_finalize_options(self):
        pkg_dir, dist = self.create_dist()
        os.chdir(pkg_dir)
        cmd = bdist_dumb(dist)
        self.assertEqual(cmd.bdist_dir, None)
        cmd.finalize_options()
        base = cmd.get_finalized_command('bdist').bdist_base
        self.assertEqual(cmd.bdist_dir, os.path.join(base, 'dumb'))
        default = cmd.default_format[os.name]
        self.assertEqual(cmd.format, default)
        return


def test_suite():
    return unittest.makeSuite(BuildDumbTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())