# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/wrapped_reflection_framework.py
from constants import IS_UE_EDITOR
from collections import namedtuple
from contextlib import contextmanager
if IS_UE_EDITOR:
    from reflection_framework import ReflectionMetaclass
    from reflection_framework import reflectedNamedTuple
    from reflection_framework import notifyPropertiesReset
else:
    ReflectionMetaclass = type
    reflectedNamedTuple = namedtuple

    @contextmanager
    def notifyPropertiesReset(obj):
        yield
        return