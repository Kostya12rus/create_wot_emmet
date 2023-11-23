# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/hangar_selectable_objects/__init__.py
from .interfaces import ISelectableObject, ISelectableLogicCallback
from .hangar_selectable_logic import HangarSelectableLogic
__all__ = ('ISelectableObject', 'ISelectableLogicCallback', 'HangarSelectableLogic')