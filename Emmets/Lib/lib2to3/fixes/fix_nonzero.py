# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_nonzero.py
from .. import fixer_base
from ..fixer_util import Name, syms

class FixNonzero(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    classdef< 'class' any+ ':'\n              suite< any*\n                     funcdef< 'def' name='__nonzero__'\n                              parameters< '(' NAME ')' > any+ >\n                     any* > >\n    "

    def transform(self, node, results):
        name = results['name']
        new = Name('__bool__', prefix=name.prefix)
        name.replace(new)