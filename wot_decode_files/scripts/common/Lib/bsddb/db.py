# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/bsddb/db.py
import sys
absolute_import = sys.version_info[0] >= 3
if not absolute_import:
    if __name__.startswith('bsddb3.'):
        from _pybsddb import *
        from _pybsddb import __version__
    else:
        from _bsddb import *
        from _bsddb import __version__
elif __name__.startswith('bsddb3.'):
    exec 'from ._pybsddb import *'
    exec 'from ._pybsddb import __version__'
else:
    exec 'from ._bsddb import *'
    exec 'from ._bsddb import __version__'