# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/moves/collections/abc.py
from __future__ import absolute_import
from future.utils import PY3
if PY3:
    from collections.abc import *
else:
    from collections import Container, Hashable, Iterable, Iterator, Sized, Callable, Sequence, MutableSequence, Set, MutableSet
    from _abcoll import MutableMapping, MappingView, ItemsView, KeysView, Mapping