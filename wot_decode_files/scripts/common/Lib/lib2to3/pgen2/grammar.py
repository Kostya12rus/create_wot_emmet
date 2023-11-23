# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/pgen2/grammar.py
import collections, pickle
from . import token, tokenize

class Grammar(object):

    def __init__(self):
        self.symbol2number = {}
        self.number2symbol = {}
        self.states = []
        self.dfas = {}
        self.labels = [
         (0, 'EMPTY')]
        self.keywords = {}
        self.tokens = {}
        self.symbol2label = {}
        self.start = 256

    def dump(self, filename):
        with open(filename, 'wb') as (f):
            d = _make_deterministic(self.__dict__)
            pickle.dump(d, f, 2)

    def load(self, filename):
        f = open(filename, 'rb')
        d = pickle.load(f)
        f.close()
        self.__dict__.update(d)

    def loads(self, pkl):
        self.__dict__.update(pickle.loads(pkl))

    def copy(self):
        new = self.__class__()
        for dict_attr in ('symbol2number', 'number2symbol', 'dfas', 'keywords', 'tokens',
                          'symbol2label'):
            setattr(new, dict_attr, getattr(self, dict_attr).copy())

        new.labels = self.labels[:]
        new.states = self.states[:]
        new.start = self.start
        return new

    def report(self):
        from pprint import pprint
        print 's2n'
        pprint(self.symbol2number)
        print 'n2s'
        pprint(self.number2symbol)
        print 'states'
        pprint(self.states)
        print 'dfas'
        pprint(self.dfas)
        print 'labels'
        pprint(self.labels)
        print 'start', self.start


def _make_deterministic(top):
    if isinstance(top, dict):
        return collections.OrderedDict(sorted((k, _make_deterministic(v)) for k, v in top.iteritems()))
    if isinstance(top, list):
        return [ _make_deterministic(e) for e in top ]
    if isinstance(top, tuple):
        return tuple(_make_deterministic(e) for e in top)
    return top


opmap_raw = '\n( LPAR\n) RPAR\n[ LSQB\n] RSQB\n: COLON\n, COMMA\n; SEMI\n+ PLUS\n- MINUS\n* STAR\n/ SLASH\n| VBAR\n& AMPER\n< LESS\n> GREATER\n= EQUAL\n. DOT\n% PERCENT\n` BACKQUOTE\n{ LBRACE\n} RBRACE\n@ AT\n@= ATEQUAL\n== EQEQUAL\n!= NOTEQUAL\n<> NOTEQUAL\n<= LESSEQUAL\n>= GREATEREQUAL\n~ TILDE\n^ CIRCUMFLEX\n<< LEFTSHIFT\n>> RIGHTSHIFT\n** DOUBLESTAR\n+= PLUSEQUAL\n-= MINEQUAL\n*= STAREQUAL\n/= SLASHEQUAL\n%= PERCENTEQUAL\n&= AMPEREQUAL\n|= VBAREQUAL\n^= CIRCUMFLEXEQUAL\n<<= LEFTSHIFTEQUAL\n>>= RIGHTSHIFTEQUAL\n**= DOUBLESTAREQUAL\n// DOUBLESLASH\n//= DOUBLESLASHEQUAL\n-> RARROW\n'
opmap = {}
for line in opmap_raw.splitlines():
    if line:
        op, name = line.split()
        opmap[op] = getattr(token, name)