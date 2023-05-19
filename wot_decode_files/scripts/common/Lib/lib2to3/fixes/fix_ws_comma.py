# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_ws_comma.py
from .. import pytree
from ..pgen2 import token
from .. import fixer_base

class FixWsComma(fixer_base.BaseFix):
    explicit = True
    PATTERN = "\n    any<(not(',') any)+ ',' ((not(',') any)+ ',')* [not(',') any]>\n    "
    COMMA = pytree.Leaf(token.COMMA, ',')
    COLON = pytree.Leaf(token.COLON, ':')
    SEPS = (COMMA, COLON)

    def transform(self, node, results):
        new = node.clone()
        comma = False
        for child in new.children:
            if child in self.SEPS:
                prefix = child.prefix
                if prefix.isspace() and '\n' not in prefix:
                    child.prefix = ''
                comma = True
            else:
                if comma:
                    prefix = child.prefix
                    if not prefix:
                        child.prefix = ' '
                comma = False

        return new