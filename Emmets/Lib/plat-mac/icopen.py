# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/icopen.py
from warnings import warnpy3k
warnpy3k('In 3.x, the icopen module is removed.', stacklevel=2)
import __builtin__
_builtin_open = globals().get('_builtin_open', __builtin__.open)

def _open_with_typer(*args):
    file = _builtin_open(*args)
    filename = args[0]
    mode = 'r'
    if args[1:]:
        mode = args[1]
    if mode[0] == 'w':
        from ic import error, settypecreator
        try:
            settypecreator(filename)
        except error:
            pass

    return file


__builtin__.open = _open_with_typer