# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_future.py
from .. import fixer_base
from ..fixer_util import BlankLine

class FixFuture(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = 'import_from< \'from\' module_name="__future__" \'import\' any >'
    run_order = 10

    def transform(self, node, results):
        new = BlankLine()
        new.prefix = node.prefix
        return new