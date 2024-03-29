# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_types.py
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name
_TYPE_MAPPING = {'BooleanType': 'bool', 
   'BufferType': 'memoryview', 
   'ClassType': 'type', 
   'ComplexType': 'complex', 
   'DictType': 'dict', 
   'DictionaryType': 'dict', 
   'EllipsisType': 'type(Ellipsis)', 
   'FloatType': 'float', 
   'IntType': 'int', 
   'ListType': 'list', 
   'LongType': 'int', 
   'ObjectType': 'object', 
   'NoneType': 'type(None)', 
   'NotImplementedType': 'type(NotImplemented)', 
   'SliceType': 'slice', 
   'StringType': 'bytes', 
   'StringTypes': '(str,)', 
   'TupleType': 'tuple', 
   'TypeType': 'type', 
   'UnicodeType': 'str', 
   'XRangeType': 'range'}
_pats = [ "power< 'types' trailer< '.' name='%s' > >" % t for t in _TYPE_MAPPING ]

class FixTypes(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = ('|').join(_pats)

    def transform(self, node, results):
        new_value = unicode(_TYPE_MAPPING.get(results['name'].value))
        if new_value:
            return Name(new_value, prefix=node.prefix)
        else:
            return