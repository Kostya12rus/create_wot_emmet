# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_raise.py
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, Attr, ArgList, is_tuple

class FixRaise(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    raise_stmt< 'raise' exc=any [',' val=any [',' tb=any]] >\n    "

    def transform(self, node, results):
        syms = self.syms
        exc = results['exc'].clone()
        if exc.type == token.STRING:
            msg = 'Python 3 does not support string exceptions'
            self.cannot_convert(node, msg)
            return
        else:
            if is_tuple(exc):
                while is_tuple(exc):
                    exc = exc.children[1].children[0].clone()

                exc.prefix = ' '
            if 'val' not in results:
                new = pytree.Node(syms.raise_stmt, [Name('raise'), exc])
                new.prefix = node.prefix
                return new
            val = results['val'].clone()
            if is_tuple(val):
                args = [ c.clone() for c in val.children[1:-1] ]
            else:
                val.prefix = ''
                args = [val]
            if 'tb' in results:
                tb = results['tb'].clone()
                tb.prefix = ''
                e = exc
                if val.type != token.NAME or val.value != 'None':
                    e = Call(exc, args)
                with_tb = Attr(e, Name('with_traceback')) + [ArgList([tb])]
                new = pytree.Node(syms.simple_stmt, [Name('raise')] + with_tb)
                new.prefix = node.prefix
                return new
            return pytree.Node(syms.raise_stmt, [
             Name('raise'), Call(exc, args)], prefix=node.prefix)