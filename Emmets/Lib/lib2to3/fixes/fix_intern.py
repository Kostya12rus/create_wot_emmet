# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_intern.py
from .. import pytree
from .. import fixer_base
from ..fixer_util import Name, Attr, touch_import

class FixIntern(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'intern'\n           trailer< lpar='('\n                    ( not(arglist | argument<any '=' any>) obj=any\n                      | obj=arglist<(not argument<any '=' any>) any ','> )\n                    rpar=')' >\n           after=any*\n    >\n    "

    def transform(self, node, results):
        if results:
            obj = results['obj']
            if obj:
                if obj.type == self.syms.star_expr:
                    return
                if obj.type == self.syms.argument and obj.children[0].value == '**':
                    return
        syms = self.syms
        obj = results['obj'].clone()
        if obj.type == syms.arglist:
            newarglist = obj.clone()
        else:
            newarglist = pytree.Node(syms.arglist, [obj.clone()])
        after = results['after']
        if after:
            after = [ n.clone() for n in after ]
        new = pytree.Node(syms.power, Attr(Name('sys'), Name('intern')) + [pytree.Node(syms.trailer, [results['lpar'].clone(), newarglist, results['rpar'].clone()])] + after)
        new.prefix = node.prefix
        touch_import(None, 'sys', node)
        return new