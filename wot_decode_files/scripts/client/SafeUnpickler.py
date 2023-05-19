# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/SafeUnpickler.py
import sys, cPickle, StringIO

class SafeUnpickler(object):
    PICKLE_SAFE = {'__builtin__': set(['object', 'set', 'frozenset', 'list', 'tuple']), 
       'datetime': set(['datetime']), 
       '_BWp': set(['Array', 'FixedDict']), 
       'Math': set(['Vector2', 'Vector3'])}

    @classmethod
    def find_class(cls, module, name):
        if module not in cls.PICKLE_SAFE:
            raise cPickle.UnpicklingError('Attempting to unpickle unsafe module %s' % module)
        __import__(module)
        mod = sys.modules[module]
        classesSet = cls.PICKLE_SAFE[module]
        if name not in classesSet or classesSet is None:
            raise cPickle.UnpicklingError('Attempting to unpickle unsafe class %s' % name)
        klass = getattr(mod, name)
        return klass

    @classmethod
    def loads(cls, pickle_string):
        pickle_obj = cPickle.Unpickler(StringIO.StringIO(pickle_string))
        pickle_obj.find_global = cls.find_class
        return pickle_obj.load()