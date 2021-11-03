# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/_builtinSuites/__init__.py
from warnings import warnpy3k
warnpy3k('In 3.x, the _builtinSuites module is removed.', stacklevel=2)
import aetools, builtin_Suite
_code_to_module = {'reqd': builtin_Suite, 
   'core': builtin_Suite}
_code_to_fullname = {'reqd': ('_builtinSuites.builtin_Suite', 'builtin_Suite'), 
   'core': ('_builtinSuites.builtin_Suite', 'builtin_Suite')}
from builtin_Suite import *

class _builtinSuites(builtin_Suite_Events, aetools.TalkTo):
    _signature = 'ascr'