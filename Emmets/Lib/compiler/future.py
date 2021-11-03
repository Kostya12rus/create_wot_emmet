# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/compiler/future.py
from compiler import ast, walk

def is_future(stmt):
    if not isinstance(stmt, ast.From):
        return 0
    else:
        if stmt.modname == '__future__':
            return 1
        return 0


class FutureParser:
    features = ('nested_scopes', 'generators', 'division', 'absolute_import', 'with_statement',
                'print_function', 'unicode_literals')

    def __init__(self):
        self.found = {}

    def visitModule(self, node):
        stmt = node.node
        for s in stmt.nodes:
            if not self.check_stmt(s):
                break

    def check_stmt(self, stmt):
        if is_future(stmt):
            for name, asname in stmt.names:
                if name in self.features:
                    self.found[name] = 1
                else:
                    raise SyntaxError, 'future feature %s is not defined' % name

            stmt.valid_future = 1
            return 1
        return 0

    def get_features(self):
        return self.found.keys()


class BadFutureParser:

    def visitFrom(self, node):
        if hasattr(node, 'valid_future'):
            return
        if node.modname != '__future__':
            return
        raise SyntaxError, 'invalid future statement ' + repr(node)


def find_futures(node):
    p1 = FutureParser()
    p2 = BadFutureParser()
    walk(node, p1)
    walk(node, p2)
    return p1.get_features()


if __name__ == '__main__':
    import sys
    from compiler import parseFile, walk
    for file in sys.argv[1:]:
        print file
        tree = parseFile(file)
        v = FutureParser()
        walk(tree, v)
        print v.found
        print