# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/resources/local/base.py
import typing, itertools
from gui.game_loading.resources.base import BaseResources
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.models import BaseResourceModel

class LocalResources(BaseResources):
    __slots__ = ('_source', '_iterator', '_cycle')

    def __init__(self, source, cycle=False):
        super(LocalResources, self).__init__()
        self._source = list(source)
        self._cycle = cycle
        self._iterator = None
        return

    def get(self):
        if self._iterator is None:
            self._iterator = self._createIterator()
        try:
            return self._iterator.next()
        except StopIteration:
            return

        return

    def reset(self):
        if self._iterator is not None:
            self._iterator = None
        super(LocalResources, self).reset()
        return

    def destroy(self):
        super(LocalResources, self).destroy()
        self._iterator = None
        return

    def _createIterator(self):
        if self._cycle:
            return itertools.cycle(self._source)
        return iter(self._source)