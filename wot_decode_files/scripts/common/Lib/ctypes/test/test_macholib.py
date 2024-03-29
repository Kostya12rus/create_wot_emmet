# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/test/test_macholib.py
import os, sys, unittest
from ctypes.macholib.dyld import dyld_find

def find_lib(name):
    possible = [
     'lib' + name + '.dylib', name + '.dylib', name + '.framework/' + name]
    for dylib in possible:
        try:
            return os.path.realpath(dyld_find(dylib))
        except ValueError:
            pass

    raise ValueError('%s not found' % (name,))


class MachOTest(unittest.TestCase):

    @unittest.skipUnless(sys.platform == 'darwin', 'OSX-specific test')
    def test_find(self):
        self.assertEqual(find_lib('pthread'), '/usr/lib/libSystem.B.dylib')
        result = find_lib('z')
        self.assertRegexpMatches(result, '.*/lib/libz\\..*.*\\.dylib')
        self.assertEqual(find_lib('IOKit'), '/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit')


if __name__ == '__main__':
    unittest.main()