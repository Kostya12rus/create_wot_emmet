# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/types.py
import sys
NoneType = type(None)
TypeType = type
ObjectType = object
IntType = int
LongType = long
FloatType = float
BooleanType = bool
try:
    ComplexType = complex
except NameError:
    pass

StringType = str
try:
    UnicodeType = unicode
    StringTypes = (StringType, UnicodeType)
except NameError:
    StringTypes = (
     StringType,)

BufferType = buffer
TupleType = tuple
ListType = list
DictType = DictionaryType = dict

def _f():
    pass


FunctionType = type(_f)
LambdaType = type((lambda : None))
CodeType = type(_f.func_code)

def _g():
    yield 1


GeneratorType = type(_g())

class _C:

    def _m(self):
        pass


ClassType = type(_C)
UnboundMethodType = type(_C._m)
_x = _C()
InstanceType = type(_x)
MethodType = type(_x._m)
BuiltinFunctionType = type(len)
BuiltinMethodType = type([].append)
ModuleType = type(sys)
FileType = file
XRangeType = xrange
try:
    raise TypeError
except TypeError:
    tb = sys.exc_info()[2]
    TracebackType = type(tb)
    FrameType = type(tb.tb_frame)
    del tb

SliceType = slice
EllipsisType = type(Ellipsis)
DictProxyType = type(TypeType.__dict__)
NotImplementedType = type(NotImplemented)
GetSetDescriptorType = type(FunctionType.func_code)
MemberDescriptorType = type(FunctionType.func_globals)
del sys
del _f
del _g
del _C
del _x
__all__ = list(n for n in globals() if n[:1] != '_')