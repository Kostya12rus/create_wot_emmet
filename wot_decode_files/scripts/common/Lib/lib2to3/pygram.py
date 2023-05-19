# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/pygram.py
import os
from .pgen2 import token
from .pgen2 import driver
from . import pytree
_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'Grammar.txt')
_PATTERN_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'PatternGrammar.txt')

class Symbols(object):

    def __init__(self, grammar):
        for name, symbol in grammar.symbol2number.iteritems():
            setattr(self, name, symbol)


python_grammar = driver.load_packaged_grammar('lib2to3', _GRAMMAR_FILE)
python_symbols = Symbols(python_grammar)
python_grammar_no_print_statement = python_grammar.copy()
del python_grammar_no_print_statement.keywords['print']
pattern_grammar = driver.load_packaged_grammar('lib2to3', _PATTERN_GRAMMAR_FILE)
pattern_symbols = Symbols(pattern_grammar)