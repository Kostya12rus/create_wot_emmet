# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/CodeWarrior/Required.py
import aetools, MacOS
_code = 'reqd'
from StdSuites.Required_Suite import *

class Required_Events(Required_Suite_Events):
    _argmap_open = {'converting': 'Conv'}

    def open(self, _object, _attributes={}, **_arguments):
        _code = 'aevt'
        _subcode = 'odoc'
        aetools.keysubst(_arguments, self._argmap_open)
        _arguments['----'] = _object
        aetools.enumsubst(_arguments, 'Conv', _Enum_Conv)
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']


_Enum_Conv = {'yes': 'yes ', 
   'no': 'no  '}
_classdeclarations = {}
_propdeclarations = {}
_compdeclarations = {}
_enumdeclarations = {'Conv': _Enum_Conv}