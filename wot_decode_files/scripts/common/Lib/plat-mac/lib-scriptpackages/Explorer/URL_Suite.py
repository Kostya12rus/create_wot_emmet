# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/Explorer/URL_Suite.py
import aetools, MacOS
_code = 'GURL'

class URL_Suite_Events:
    _argmap_GetURL = {'to': 'dest'}

    def GetURL(self, _object, _attributes={}, **_arguments):
        _code = 'GURL'
        _subcode = 'GURL'
        aetools.keysubst(_arguments, self._argmap_GetURL)
        _arguments['----'] = _object
        _reply, _arguments, _attributes = self.send(_code, _subcode, _arguments, _attributes)
        if _arguments.get('errn', 0):
            raise aetools.Error, aetools.decodeerror(_arguments)
        if _arguments.has_key('----'):
            return _arguments['----']


_classdeclarations = {}
_propdeclarations = {}
_compdeclarations = {}
_enumdeclarations = {}