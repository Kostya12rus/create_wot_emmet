# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_input.py
from .. import fixer_base
from ..fixer_util import Call, Name
from .. import patcomp
context = patcomp.compile_pattern("power< 'eval' trailer< '(' any ')' > >")

class FixInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'input' args=trailer< '(' [any] ')' > >\n              "

    def transform(self, node, results):
        if context.match(node.parent.parent):
            return
        new = node.clone()
        new.prefix = ''
        return Call(Name('eval'), [new], prefix=node.prefix)