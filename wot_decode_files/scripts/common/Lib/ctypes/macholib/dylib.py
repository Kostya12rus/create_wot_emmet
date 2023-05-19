# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/ctypes/macholib/dylib.py
import re
__all__ = [
 'dylib_info']
DYLIB_RE = re.compile('(?x)\n(?P<location>^.*)(?:^|/)\n(?P<name>\n    (?P<shortname>\\w+?)\n    (?:\\.(?P<version>[^._]+))?\n    (?:_(?P<suffix>[^._]+))?\n    \\.dylib$\n)\n')

def dylib_info(filename):
    is_dylib = DYLIB_RE.match(filename)
    if not is_dylib:
        return None
    else:
        return is_dylib.groupdict()


def test_dylib_info():

    def d(location=None, name=None, shortname=None, version=None, suffix=None):
        return dict(location=location, name=name, shortname=shortname, version=version, suffix=suffix)

    return


if __name__ == '__main__':
    test_dylib_info()