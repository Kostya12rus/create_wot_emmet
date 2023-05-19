# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_imports2.py
from . import fix_imports
MAPPING = {'whichdb': 'dbm', 
   'anydbm': 'dbm'}

class FixImports2(fix_imports.FixImports):
    run_order = 7
    mapping = MAPPING