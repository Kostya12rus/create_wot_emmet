# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/Crypto/Util/py21compat.py
__revision__ = '$Id$'
__all__ = []
import sys, __builtin__
try:
    (
     True, False)
except NameError:
    True, False = (1, 0)
    __all__ += ['True', 'False']

try:
    object
except NameError:

    class object:
        pass


    __all__ += ['object']

try:
    isinstance(5, (int, long))
except TypeError:
    __all__ += ['isinstance']
    _builtin_type_map = {tuple: type(()), 
       list: type([]), 
       str: type(''), 
       unicode: type(''), 
       int: type(0), 
       long: type(0)}

    def isinstance(obj, t):
        if not __builtin__.isinstance(t, type(())):
            return __builtin__.isinstance(obj, _builtin_type_map.get(t, t))
        else:
            for typ in t:
                if __builtin__.isinstance(obj, _builtin_type_map.get(typ, typ)):
                    return True

            return False


try:

    class A:

        def a():
            pass

        a = staticmethod(a)


except NameError:

    class staticmethod:

        def __init__(self, anycallable):
            self.__call__ = anycallable


    __all__ += ['staticmethod']