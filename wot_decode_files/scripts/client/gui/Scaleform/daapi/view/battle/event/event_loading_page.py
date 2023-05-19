# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/event_loading_page.py
from helpers import dependency
from gui.battle_control.arena_info.interfaces import IArenaLoadController
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.Scaleform.daapi.view.bootcamp.bc_intro_page import BCIntroPage

class EventLoadingPage(BCIntroPage, IArenaLoadController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _populate(self):
        super(EventLoadingPage, self)._populate()
        self.sessionProvider.addArenaCtrl(self)

    def _dispose(self):
        self.sessionProvider.removeArenaCtrl(self)
        super(EventLoadingPage, self)._dispose()

    def updateSpaceLoadProgress(self, progress):
        self.as_updateProgressS(progress)

    def videoFinished(self):
        pass