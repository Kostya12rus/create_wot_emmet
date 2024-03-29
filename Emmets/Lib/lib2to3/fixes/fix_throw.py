# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_throw.py
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ArgList, Attr, is_tuple

class FixThrow(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< any trailer< '.' 'throw' >\n           trailer< '(' args=arglist< exc=any ',' val=any [',' tb=any] > ')' >\n    >\n    |\n    power< any trailer< '.' 'throw' > trailer< '(' exc=any ')' > >\n    "

    def transform(self, node, results):
        syms = self.syms
        exc = results['exc'].clone()
        if exc.type is token.STRING:
            self.cannot_convert(node, 'Python 3 does not support string exceptions')
            return
        else:
            val = results.get('val')
            if val is None:
                return
            val = val.clone()
            if is_tuple(val):
                args = [ c.clone() for c in val.children[1:-1] ]
            else:
                val.prefix = ''
                args = [val]
            throw_args = results['args']
            if 'tb' in results:
                tb = results['tb'].clone()
                tb.prefix = ''
                e = Call(exc, args)
                with_tb = Attr(e, Name('with_traceback')) + [ArgList([tb])]
                throw_args.replace(pytree.Node(syms.power, with_tb))
            else:
                throw_args.replace(Call(exc, args))
            return