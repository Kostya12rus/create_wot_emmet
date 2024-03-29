# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_next.py
from ..pgen2 import token
from ..pygram import python_symbols as syms
from .. import fixer_base
from ..fixer_util import Name, Call, find_binding
bind_warning = 'Calls to builtin next() possibly shadowed by global binding'

class FixNext(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< base=any+ trailer< '.' attr='next' > trailer< '(' ')' > >\n    |\n    power< head=any+ trailer< '.' attr='next' > not trailer< '(' ')' > >\n    |\n    classdef< 'class' any+ ':'\n              suite< any*\n                     funcdef< 'def'\n                              name='next'\n                              parameters< '(' NAME ')' > any+ >\n                     any* > >\n    |\n    global=global_stmt< 'global' any* 'next' any* >\n    "
    order = 'pre'

    def start_tree(self, tree, filename):
        super(FixNext, self).start_tree(tree, filename)
        n = find_binding('next', tree)
        if n:
            self.warning(n, bind_warning)
            self.shadowed_next = True
        else:
            self.shadowed_next = False

    def transform(self, node, results):
        base = results.get('base')
        attr = results.get('attr')
        name = results.get('name')
        if base:
            if self.shadowed_next:
                attr.replace(Name('__next__', prefix=attr.prefix))
            else:
                base = [ n.clone() for n in base ]
                base[0].prefix = ''
                node.replace(Call(Name('next', prefix=node.prefix), base))
        elif name:
            n = Name('__next__', prefix=name.prefix)
            name.replace(n)
        elif attr:
            if is_assign_target(node):
                head = results['head']
                if ('').join([ str(n) for n in head ]).strip() == '__builtin__':
                    self.warning(node, bind_warning)
                return
            attr.replace(Name('__next__'))
        elif 'global' in results:
            self.warning(node, bind_warning)
            self.shadowed_next = True


def is_assign_target(node):
    assign = find_assign(node)
    if assign is None:
        return False
    else:
        for child in assign.children:
            if child.type == token.EQUAL:
                return False
            if is_subtree(child, node):
                return True

        return False


def find_assign(node):
    if node.type == syms.expr_stmt:
        return node
    else:
        if node.type == syms.simple_stmt or node.parent is None:
            return
        return find_assign(node.parent)


def is_subtree(root, node):
    if root == node:
        return True
    return any(is_subtree(c, node) for c in root.children)