# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/dependency.py
from importlib import import_module
from types import ModuleType
from typing import List
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


__all__ = ('dependencyImporter', )