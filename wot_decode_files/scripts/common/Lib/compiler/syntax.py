# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/compiler/syntax.py
from compiler import ast, walk

def check(tree, multi=None):
    v = SyntaxErrorChecker(multi)
    walk(tree, v)
    return v.errors


class SyntaxErrorChecker:

    def __init__(self, multi=None):
        self.multi = multi
        self.errors = 0

    def error(self, node, msg):
        self.errors = self.errors + 1
        if self.multi is not None:
            print '%s:%s: %s' % (node.filename, node.lineno, msg)
        else:
            raise SyntaxError, '%s (%s:%s)' % (msg, node.filename, node.lineno)
        return

    def visitAssign(self, node):
        pass