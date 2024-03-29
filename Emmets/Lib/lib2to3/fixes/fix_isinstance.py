# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_isinstance.py
from .. import fixer_base
from ..fixer_util import token

class FixIsinstance(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power<\n        'isinstance'\n        trailer< '(' arglist< any ',' atom< '('\n            args=testlist_gexp< any+ >\n        ')' > > ')' >\n    >\n    "
    run_order = 6

    def transform(self, node, results):
        names_inserted = set()
        testlist = results['args']
        args = testlist.children
        new_args = []
        iterator = enumerate(args)
        for idx, arg in iterator:
            if arg.type == token.NAME and arg.value in names_inserted:
                if idx < len(args) - 1 and args[idx + 1].type == token.COMMA:
                    iterator.next()
                    continue
            else:
                new_args.append(arg)
                if arg.type == token.NAME:
                    names_inserted.add(arg.value)

        if new_args and new_args[-1].type == token.COMMA:
            del new_args[-1]
        if len(new_args) == 1:
            atom = testlist.parent
            new_args[0].prefix = atom.prefix
            atom.replace(new_args[0])
        else:
            args[:] = new_args
            node.changed()