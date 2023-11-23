# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/login_screen.py
import typing, game_loading_bindings
from frameworks.state_machine import StateFlags
from gui.game_loading.state_machine.const import GameLoadingStates
from gui.game_loading.state_machine.models import ImageViewSettingsModel
from gui.game_loading.state_machine.states.slide import StaticSlideState
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.cdn.images import CdnImagesResources

class LoginScreenState(StaticSlideState):
    __slots__ = ('_nextSlideDuration', )

    def __init__(self, images, nextSlideDuration, viewSettings):
        super(LoginScreenState, self).__init__(stateID=GameLoadingStates.LOGIN_SCREEN.value, flags=StateFlags.UNDEFINED, images=images, imageViewSettings=viewSettings)
        self._nextSlideDuration = nextSlideDuration

    @property
    def nextSlideDuration(self):
        return self._nextSlideDuration

    def _onEntered(self):
        super(LoginScreenState, self)._onEntered()
        game_loading_bindings.bringLoadingViewToBottom()