# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_filter.py
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ListComp, in_special_context

class FixFilter(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = "\n    filter_lambda=power<\n        'filter'\n        trailer<\n            '('\n            arglist<\n                lambdef< 'lambda'\n                         (fp=NAME | vfpdef< '(' fp=NAME ')'> ) ':' xp=any\n                >\n                ','\n                it=any\n            >\n            ')'\n        >\n    >\n    |\n    power<\n        'filter'\n        trailer< '(' arglist< none='None' ',' seq=any > ')' >\n    >\n    |\n    power<\n        'filter'\n        args=trailer< '(' [any] ')' >\n    >\n    "
    skip_on = 'future_builtins.filter'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        else:
            if 'filter_lambda' in results:
                new = ListComp(results.get('fp').clone(), results.get('fp').clone(), results.get('it').clone(), results.get('xp').clone())
            elif 'none' in results:
                new = ListComp(Name('_f'), Name('_f'), results['seq'].clone(), Name('_f'))
            else:
                if in_special_context(node):
                    return None
                new = node.clone()
                new.prefix = ''
                new = Call(Name('list'), [new])
            new.prefix = node.prefix
            return new