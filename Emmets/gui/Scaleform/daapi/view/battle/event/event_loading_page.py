# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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