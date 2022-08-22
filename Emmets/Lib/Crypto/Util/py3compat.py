# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Util/py3compat.py
__revision__ = '$Id$'
import sys
if sys.version_info[0] == 2:
    from types import UnicodeType as _UnicodeType

    def b(s):
        return s


    def bchr(s):
        return chr(s)


    def bstr(s):
        return str(s)


    def bord(s):
        return ord(s)


    def tobytes(s):
        if isinstance(s, _UnicodeType):
            return s.encode('latin-1')
        else:
            return ('').join(s)


    def tostr(bs):
        return unicode(bs, 'latin-1')


    from StringIO import StringIO as BytesIO
else:

    def b(s):
        return s.encode('latin-1')


    def bchr(s):
        return bytes([s])


    def bstr(s):
        if isinstance(s, str):
            return bytes(s, 'latin-1')
        else:
            return bytes(s)


    def bord(s):
        return s


    def tobytes(s):
        if isinstance(s, bytes):
            return s
        else:
            if isinstance(s, str):
                return s.encode('latin-1')
            return bytes(s)


    def tostr(bs):
        return bs.decode('latin-1')


    from io import BytesIO