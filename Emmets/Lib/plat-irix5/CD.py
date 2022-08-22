# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-irix5/CD.py
from warnings import warnpy3k
warnpy3k('the CD module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
ERROR = 0
NODISC = 1
READY = 2
PLAYING = 3
PAUSED = 4
STILL = 5
AUDIO = 0
PNUM = 1
INDEX = 2
PTIME = 3
ATIME = 4
CATALOG = 5
IDENT = 6
CONTROL = 7
CDDA_DATASIZE = 2352