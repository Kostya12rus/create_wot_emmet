# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/dependency.py
import sys, typing
from importlib import import_module
from types import ModuleType
from constants import IS_VS_EDITOR
if IS_VS_EDITOR:

    class MockObjectMeta(type):

        def __getitem__(cls, item):
            return MockObject

        def __getattr__(cls, item):
            return MockObject

        def __iter__(cls):
            while False:
                yield

            return


    class MockObject(object):
        __metaclass__ = MockObjectMeta

        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, *args, **kwargs):
            return MockObject()

        def __getitem__(self, item):
            return MockObject()

        def __getattr__(self, item):
            return MockObject()

        def __iter__(self):
            while False:
                yield

            return

        def __str__(self):
            return ''


    MOCK_IMPORT_ERRORS = []

    def tryImportGen(modules):
        for module in modules:
            try:
                yield import_module(module)
            except ImportError as er:
                MOCK_IMPORT_ERRORS.append('On import module <%s> was raised ImportError with msg - %s' % (module, er.message))
                yield MockObject


def dependencyImporter(*modules):
    if IS_VS_EDITOR:
        return list(tryImportGen(modules))
    return [ import_module(module) for module in modules ]


def dependencyMocker(*modules):
    if IS_VS_EDITOR:
        for module in modules:
            if isinstance(module, tuple):
                path, mock = module
            else:
                path, mock = module, MockObject()
            sys.modules[path] = mock


__all__ = ('dependencyImporter', 'dependencyMocker')