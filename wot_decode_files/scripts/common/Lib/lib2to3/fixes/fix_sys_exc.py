# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_sys_exc.py
from .. import fixer_base
from ..fixer_util import Attr, Call, Name, Number, Subscript, Node, syms

class FixSysExc(fixer_base.BaseFix):
    exc_info = [
     'exc_type', 'exc_value', 'exc_traceback']
    BM_compatible = True
    PATTERN = "\n              power< 'sys' trailer< dot='.' attribute=(%s) > >\n              " % ('|').join("'%s'" % e for e in exc_info)

    def transform(self, node, results):
        sys_attr = results['attribute'][0]
        index = Number(self.exc_info.index(sys_attr.value))
        call = Call(Name('exc_info'), prefix=sys_attr.prefix)
        attr = Attr(Name('sys'), call)
        attr[1].children[0].prefix = results['dot'].prefix
        attr.append(Subscript(index))
        return Node(syms.power, attr, prefix=node.prefix)