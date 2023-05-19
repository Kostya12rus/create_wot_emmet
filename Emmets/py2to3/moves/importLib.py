# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/moves/importLib.py
from __future__ import absolute_import
from py2to3.utils import PY3
if PY3:
    from importlib import reload
else:
    from __builtin__ import reload