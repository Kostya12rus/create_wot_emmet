# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/statvfs.py
from warnings import warnpy3k
warnpy3k('the statvfs module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
F_BSIZE = 0
F_FRSIZE = 1
F_BLOCKS = 2
F_BFREE = 3
F_BAVAIL = 4
F_FILES = 5
F_FFREE = 6
F_FAVAIL = 7
F_FLAG = 8
F_NAMEMAX = 9