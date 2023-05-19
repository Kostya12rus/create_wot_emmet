# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_apply.py
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Call, Comma, parenthesize

class FixApply(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< 'apply'\n        trailer<\n            '('\n            arglist<\n                (not argument<NAME '=' any>) func=any ','\n                (not argument<NAME '=' any>) args=any [','\n                (not argument<NAME '=' any>) kwds=any] [',']\n            >\n            ')'\n        >\n    >\n    "

    def transform(self, node, results):
        syms = self.syms
        func = results['func']
        args = results['args']
        kwds = results.get('kwds')
        if args:
            if args.type == self.syms.star_expr:
                return
            if args.type == self.syms.argument and args.children[0].value == '**':
                return
        if kwds and kwds.type == self.syms.argument and kwds.children[0].value == '**':
            return
        else:
            prefix = node.prefix
            func = func.clone()
            if func.type not in (token.NAME, syms.atom) and (func.type != syms.power or func.children[-2].type == token.DOUBLESTAR):
                func = parenthesize(func)
            func.prefix = ''
            args = args.clone()
            args.prefix = ''
            if kwds is not None:
                kwds = kwds.clone()
                kwds.prefix = ''
            l_newargs = [
             pytree.Leaf(token.STAR, '*'), args]
            if kwds is not None:
                l_newargs.extend([Comma(),
                 pytree.Leaf(token.DOUBLESTAR, '**'),
                 kwds])
                l_newargs[-2].prefix = ' '
            return Call(func, l_newargs, prefix=prefix)