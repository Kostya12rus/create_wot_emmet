# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-irix5/WAIT.py
from warnings import warnpy3k
warnpy3k('the WAIT module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
_WSTOPPED = 127
WNOHANG = 64
WEXITED = 1
WTRAPPED = 2
WSTOPPED = 4
WCONTINUED = 8
WNOWAIT = 128
WOPTMASK = WEXITED | WTRAPPED | WSTOPPED | WCONTINUED | WNOHANG | WNOWAIT
WSTOPFLG = 127
WCONTFLG = 65535
WCOREFLAG = 128
WSIGMASK = 127
WUNTRACED = 4