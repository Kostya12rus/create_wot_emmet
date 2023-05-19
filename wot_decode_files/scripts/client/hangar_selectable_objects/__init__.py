# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/hangar_selectable_objects/__init__.py
from .interfaces import ISelectableObject, ISelectableLogicCallback
from .hangar_selectable_logic import HangarSelectableLogic
__all__ = ('ISelectableObject', 'ISelectableLogicCallback', 'HangarSelectableLogic')