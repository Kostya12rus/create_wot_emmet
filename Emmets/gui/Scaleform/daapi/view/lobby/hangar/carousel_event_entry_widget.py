# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousel_event_entry_widget.py
import itertools, typing
from gui.Scaleform.daapi.view.meta.CarouselEventEntryMeta import CarouselEventEntryMeta
from gui.impl.gen import R
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.base.listener import IPrbListener
from gui.shared.system_factory import collectCarouselEventEntryPoints
if typing.TYPE_CHECKING:
    from typing import Dict, Type
    from skeletons.gui.hangar import ICarouselEventEntry
_VIEWS = {}

class CarouselEventEntryHolder(CarouselEventEntryMeta, IPrbListener):

    def __init__(self):
        super(CarouselEventEntryHolder, self).__init__()
        self.__activeViewID = R.invalid()

    def updateState(self):
        activeViewID = _getActiveCarouselEventEntryID()
        if self.__activeViewID != activeViewID:
            self.__activeViewID = activeViewID
            self._destroyInjected()
            if activeViewID != R.invalid():
                self._createInjectView(self.__activeViewID)

    def _onPopulate(self):
        self.updateState()

    def _makeInjectView(self, viewID=None):
        view = _VIEWS.get(viewID) or collectCarouselEventEntryPoints().get(viewID)
        return view()


def isAnyEntryVisible():
    return _getActiveCarouselEventEntryID() != R.invalid()


def _getActiveCarouselEventEntryID():
    entries = collectCarouselEventEntryPoints()
    state = g_prbLoader.getDispatcher().getFunctionalState()
    for viewID, view in itertools.chain(_VIEWS.iteritems(), entries.iteritems()):
        if view.getIsActive(state):
            return viewID

    return R.invalid()