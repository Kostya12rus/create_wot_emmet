# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_numliterals.py
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Number

class FixNumliterals(fixer_base.BaseFix):
    _accept_type = token.NUMBER

    def match(self, node):
        return node.value.startswith('0') or node.value[-1] in 'Ll'

    def transform(self, node, results):
        val = node.value
        if val[-1] in 'Ll':
            val = val[:-1]
        elif val.startswith('0') and val.isdigit() and len(set(val)) > 1:
            val = '0o' + val[1:]
        return Number(val, prefix=node.prefix)