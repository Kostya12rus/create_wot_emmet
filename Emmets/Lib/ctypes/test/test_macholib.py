# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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
    if sys.platform == 'darwin':

        def test_find(self):
            self.assertEqual(find_lib('pthread'), '/usr/lib/libSystem.B.dylib')
            result = find_lib('z')
            self.assertRegexpMatches(result, '.*/lib/libz\\..*.*\\.dylib')
            self.assertEqual(find_lib('IOKit'), '/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit')


if __name__ == '__main__':
    unittest.main()