# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/event_boards/__init__.py
from skeletons.gui.event_boards_controllers import IEventBoardController
__all__ = ('getEventServicesConfig', )

def getEventServicesConfig(manager):
    from gui.event_boards.event_boards_controller import EventBoardsController
    ctrl = EventBoardsController()
    manager.addInstance(IEventBoardController, ctrl, finalizer='fini')