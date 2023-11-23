# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_imports2.py
from . import fix_imports
MAPPING = {'whichdb': 'dbm', 
   'anydbm': 'dbm'}

class FixImports2(fix_imports.FixImports):
    run_order = 7
    mapping = MAPPING