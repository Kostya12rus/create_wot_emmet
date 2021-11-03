# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/preview_selectable_logic.py
from ClientSelectableRankedObject import ClientSelectableRankedObject
from hangar_selectable_objects import HangarSelectableLogic

class PreviewSelectableLogic(HangarSelectableLogic):

    def _filterEntity(self, entity):
        isFiltered = super(PreviewSelectableLogic, self)._filterEntity(entity)
        isFiltered = isFiltered and not isinstance(entity, ClientSelectableRankedObject)
        return isFiltered