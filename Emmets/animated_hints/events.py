# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/animated_hints/events.py
import typing
from gui.shared.events import HasCtxEvent
if typing.TYPE_CHECKING:
    from animated_hints.constants import EventAction

class HintActionEvent(HasCtxEvent):
    EVENT_TYPE = 'animated_hint_action_event'

    def __init__(self, action, ctx=None):
        super(HintActionEvent, self).__init__(eventType=self.EVENT_TYPE, ctx=ctx)
        self.action = action