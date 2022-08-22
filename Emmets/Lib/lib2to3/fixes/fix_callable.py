# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_callable.py
from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, String, Attr, touch_import

class FixCallable(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'callable'\n           trailer< lpar='('\n                    ( not(arglist | argument<any '=' any>) func=any\n                      | func=arglist<(not argument<any '=' any>) any ','> )\n                    rpar=')' >\n           after=any*\n    >\n    "

    def transform(self, node, results):
        func = results['func']
        touch_import(None, 'collections', node=node)
        args = [
         func.clone(), String(', ')]
        args.extend(Attr(Name('collections'), Name('Callable')))
        return Call(Name('isinstance'), args, prefix=node.prefix)