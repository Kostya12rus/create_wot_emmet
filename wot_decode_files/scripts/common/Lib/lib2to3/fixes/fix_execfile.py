# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_execfile.py
from .. import fixer_base
from ..fixer_util import Comma, Name, Call, LParen, RParen, Dot, Node, ArgList, String, syms

class FixExecfile(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< 'execfile' trailer< '(' arglist< filename=any [',' globals=any [',' locals=any ] ] > ')' > >\n    |\n    power< 'execfile' trailer< '(' filename=any ')' > >\n    "

    def transform(self, node, results):
        filename = results['filename']
        globals = results.get('globals')
        locals = results.get('locals')
        execfile_paren = node.children[-1].children[-1].clone()
        open_args = ArgList([filename.clone(), Comma(), String('"rb"', ' ')], rparen=execfile_paren)
        open_call = Node(syms.power, [Name('open'), open_args])
        read = [Node(syms.trailer, [Dot(), Name('read')]),
         Node(syms.trailer, [LParen(), RParen()])]
        open_expr = [open_call] + read
        filename_arg = filename.clone()
        filename_arg.prefix = ' '
        exec_str = String("'exec'", ' ')
        compile_args = open_expr + [Comma(), filename_arg, Comma(), exec_str]
        compile_call = Call(Name('compile'), compile_args, '')
        args = [
         compile_call]
        if globals is not None:
            args.extend([Comma(), globals.clone()])
        if locals is not None:
            args.extend([Comma(), locals.clone()])
        return Call(Name('exec'), args, prefix=node.prefix)