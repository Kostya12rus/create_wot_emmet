# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/TournamentsView.py
from typing import TYPE_CHECKING
from gui.Scaleform.daapi.view.lobby import BrowserView
from gui.tournament.sound_constants import TOURNAMENTS_SOUND_SPACE
if TYPE_CHECKING:
    pass

class TournamentsView(BrowserView):
    __background_alpha__ = 1.0
    _BROWSER_SOUND_SPACE = TOURNAMENTS_SOUND_SPACE

    def _checkDestroy(self):
        pass