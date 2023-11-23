# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/user.py
from warnings import warnpy3k
warnpy3k('the user module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os
home = os.curdir
if 'HOME' in os.environ:
    home = os.environ['HOME']
else:
    if os.name == 'posix':
        home = os.path.expanduser('~/')
    elif os.name == 'nt':
        if 'HOMEPATH' in os.environ:
            if 'HOMEDRIVE' in os.environ:
                home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
            else:
                home = os.environ['HOMEPATH']
    pythonrc = os.path.join(home, '.pythonrc.py')
    try:
        f = open(pythonrc)
    except IOError:
        pass

    f.close()
    execfile(pythonrc)