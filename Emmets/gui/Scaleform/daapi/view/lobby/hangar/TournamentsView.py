# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/TournamentsView.py
from typing import TYPE_CHECKING
from gui.Scaleform.daapi.view.lobby import BrowserView
from gui.tournament.sound_constants import TOURNAMENTS_SOUND_SPACE
if TYPE_CHECKING:
    pass

class TournamentsView(BrowserView):
    __background_alpha__ = 1.0
    _COMMON_SOUND_SPACE = TOURNAMENTS_SOUND_SPACE

    def _checkDestroy(self):
        pass