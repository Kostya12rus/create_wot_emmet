# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_exitfunc.py
from lib2to3 import pytree, fixer_base
from lib2to3.fixer_util import Name, Attr, Call, Comma, Newline, syms

class FixExitfunc(fixer_base.BaseFix):
    keep_line_order = True
    BM_compatible = True
    PATTERN = "\n              (\n                  sys_import=import_name<'import'\n                      ('sys'\n                      |\n                      dotted_as_names< (any ',')* 'sys' (',' any)* >\n                      )\n                  >\n              |\n                  expr_stmt<\n                      power< 'sys' trailer< '.' 'exitfunc' > >\n                  '=' func=any >\n              )\n              "

    def __init__(self, *args):
        super(FixExitfunc, self).__init__(*args)

    def start_tree(self, tree, filename):
        super(FixExitfunc, self).start_tree(tree, filename)
        self.sys_import = None
        return

    def transform(self, node, results):
        if 'sys_import' in results:
            if self.sys_import is None:
                self.sys_import = results['sys_import']
            return
        func = results['func'].clone()
        func.prefix = ''
        register = pytree.Node(syms.power, Attr(Name('atexit'), Name('register')))
        call = Call(register, [func], node.prefix)
        node.replace(call)
        if self.sys_import is None:
            self.warning(node, "Can't find sys import; Please add an atexit import at the top of your file.")
            return
        else:
            names = self.sys_import.children[1]
            if names.type == syms.dotted_as_names:
                names.append_child(Comma())
                names.append_child(Name('atexit', ' '))
            else:
                containing_stmt = self.sys_import.parent
                position = containing_stmt.children.index(self.sys_import)
                stmt_container = containing_stmt.parent
                new_import = pytree.Node(syms.import_name, [
                 Name('import'), Name('atexit', ' ')])
                new = pytree.Node(syms.simple_stmt, [new_import])
                containing_stmt.insert_child(position + 1, Newline())
                containing_stmt.insert_child(position + 2, new)
            return