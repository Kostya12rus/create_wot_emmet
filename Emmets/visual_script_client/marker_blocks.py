# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/marker_blocks.py
from visual_script.block import Block, Meta
from visual_script.slot_types import SLOT_TYPE
from visual_script.misc import ASPECT
from constants import IS_VS_EDITOR
if not IS_VS_EDITOR:
    from HintManager import HintManager

class MarkerMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 6750207

    @classmethod
    def blockCategory(cls):
        return 'Hint'

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/attention'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class ShowMarker(Block, MarkerMeta):

    def __init__(self, *args, **kwargs):
        super(ShowMarker, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self.__onShow)
        self._marker = self._makeDataInputSlot('marker', SLOT_TYPE.MARKER_POINT)
        self._out = self._makeEventOutputSlot('out')

    def __onShow(self):
        if not IS_VS_EDITOR:
            marker = self._marker.getValue()
            if marker:
                HintManager.hintManager().addMarker(marker)
                HintManager.hintManager().showMarker(marker)
        self._out.call()


class HideMarker(Block, MarkerMeta):

    def __init__(self, *args, **kwargs):
        super(HideMarker, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self.__onHide)
        self._marker = self._makeDataInputSlot('marker', SLOT_TYPE.MARKER_POINT)
        self._out = self._makeEventOutputSlot('out')

    def __onHide(self):
        if not IS_VS_EDITOR:
            marker = self._marker.getValue()
            if marker:
                HintManager.hintManager().hideMarker(marker)
        self._out.call()


class IsMarkerVisible(Block, MarkerMeta):

    def __init__(self, *args, **kwargs):
        super(IsMarkerVisible, self).__init__(*args, **kwargs)
        self._marker = self._makeDataInputSlot('marker', SLOT_TYPE.MARKER_POINT)
        self._visible = self._makeDataOutputSlot('visible', SLOT_TYPE.BOOL, self._isVisible)

    def _isVisible(self):
        if not IS_VS_EDITOR:
            marker = self._marker.getValue()
            if marker:
                visible = HintManager.hintManager().isMarkerVisible(marker)
                self._visible.setValue(visible)