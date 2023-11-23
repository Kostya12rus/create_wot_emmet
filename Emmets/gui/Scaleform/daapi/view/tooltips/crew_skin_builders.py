# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/crew_skin_builders.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import crew_skin
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

class CrewSkinTooltipBuilder(DataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage):
        super(CrewSkinTooltipBuilder, self).__init__(tooltipType, linkage, crew_skin.CrewSkinTooltipDataBlock(contexts.CrewSkinContext()))

    def _buildData(self, _advanced, crewSkinID, *args, **kwargs):
        return super(CrewSkinTooltipBuilder, self)._buildData(_advanced, crewSkinID)


def getTooltipBuilders():
    return (
     CrewSkinTooltipBuilder(TOOLTIPS_CONSTANTS.CREW_SKIN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),)