# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/commands.py
from warnings import warnpy3k
warnpy3k('the commands module has been removed in Python 3.0; use the subprocess module instead', stacklevel=2)
del warnpy3k
__all__ = [
 'getstatusoutput', 'getoutput', 'getstatus']

def getstatus(file):
    import warnings
    warnings.warn('commands.getstatus() is deprecated', DeprecationWarning, 2)
    return getoutput('ls -ld' + mkarg(file))


def getoutput(cmd):
    return getstatusoutput(cmd)[1]


def getstatusoutput(cmd):
    import os
    pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None:
        sts = 0
    if text[-1:] == '\n':
        text = text[:-1]
    return (
     sts, text)


def mk2arg(head, x):
    import os
    return mkarg(os.path.join(head, x))


def mkarg(x):
    if "'" not in x:
        return " '" + x + "'"
    s = ' "'
    for c in x:
        if c in '\\$"`':
            s = s + '\\'
        s = s + c

    s = s + '"'
    return s