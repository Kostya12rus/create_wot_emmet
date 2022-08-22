# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/battle_modifiers/battle_modifier_helpers.py
from typing import Callable, Union, Dict
from battle_modifier_constants import UseType

def makeUseTypeMethods(method, copy=False):
    if isinstance(method, dict):
        if copy:
            return method.copy()
        return method
    return dict((useType, method) for useType in UseType.ALL)