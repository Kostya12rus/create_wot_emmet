# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/setuptools_extension.py
from distutils.core import Extension as _Extension
from distutils.core import Distribution as _Distribution

def _get_unpatched(cls):
    while cls.__module__.startswith('setuptools'):
        cls, = cls.__bases__

    assert cls.__module__.startswith('distutils'), 'distutils has already been patched by %r' % cls
    return cls


_Distribution = _get_unpatched(_Distribution)
_Extension = _get_unpatched(_Extension)
try:
    from Pyrex.Distutils.build_ext import build_ext
except ImportError:
    have_pyrex = False
else:
    have_pyrex = True

class Extension(_Extension):
    if not have_pyrex:

        def __init__(self, *args, **kw):
            _Extension.__init__(self, *args, **kw)
            sources = []
            for s in self.sources:
                if s.endswith('.pyx'):
                    sources.append(s[:-3] + 'c')
                else:
                    sources.append(s)

            self.sources = sources


class Library(Extension):
    pass


import sys, distutils.core, distutils.extension
distutils.core.Extension = Extension
distutils.extension.Extension = Extension
if 'distutils.command.build_ext' in sys.modules:
    sys.modules['distutils.command.build_ext'].Extension = Extension