# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCCrew.py
from gui.Scaleform.daapi.view.lobby.hangar.Crew import Crew

class BCCrew(Crew):

    def __init__(self, ctx=None):
        super(BCCrew, self).__init__()
        self._showRecruit = False

    def onShowRecruitWindowClick(self, _, __):
        pass