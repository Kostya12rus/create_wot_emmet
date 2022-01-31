# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/new_year/custom_selectable_logic.py
from HangarPoster import HangarPoster
from NewYearCelebrityEntryObject import NewYearCelebrityEntryObject
from NewYearCelebrityObject import NewYearCelebrityObject
from NewYearJukeboxSelectableObject import NewYearJukeboxSelectableObject
from NewYearSelectableObject import NewYearSelectableObject
from hangar_selectable_objects import HangarSelectableLogic

class WithoutNewYearObjectsSelectableLogic(HangarSelectableLogic):
    __slots__ = ()

    def _filterEntity(self, entity):
        if isinstance(entity, NewYearSelectableObject):
            return False
        if isinstance(entity, (NewYearCelebrityObject, NewYearCelebrityEntryObject)):
            return False
        if isinstance(entity, HangarPoster):
            return False
        if isinstance(entity, NewYearJukeboxSelectableObject):
            return False
        return super(WithoutNewYearObjectsSelectableLogic, self)._filterEntity(entity)