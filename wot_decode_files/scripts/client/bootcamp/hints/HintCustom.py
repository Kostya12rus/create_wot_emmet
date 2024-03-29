# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/hints/HintCustom.py
from HintsBase import HintBase, HINT_COMMAND

class HintCustom(HintBase):
    __ACTION_NONE = 0
    __ACTION_SHOW = 1
    __ACTION_HIDE = 2
    __ACTION_COMPLETE = 3

    def __init__(self, avatar, hintId, timeCompleted, cooldownAfter, message, voiceover=None):
        super(HintCustom, self).__init__(avatar, hintId, 0.0)
        self.__action = HintCustom.__ACTION_NONE
        self.timeCompleted = timeCompleted
        self.cooldownAfter = cooldownAfter
        self.message = message
        self.voiceover = voiceover

    def start(self):
        self._state = HintBase.STATE_DEFAULT

    def stop(self):
        self._state = HintBase.STATE_INACTIVE

    def show(self):
        if self._state not in (HintBase.STATE_HINT, self._state == HintBase.STATE_INACTIVE):
            self.__action = HintCustom.__ACTION_SHOW

    def hide(self):
        if self._state != HintBase.STATE_INACTIVE:
            self.__action = HintCustom.__ACTION_HIDE

    def complete(self):
        if self._state != HintBase.STATE_INACTIVE:
            self.__action = HintCustom.__ACTION_COMPLETE

    def update(self):
        if self._state == HintBase.STATE_INACTIVE:
            self.__action = HintCustom.__ACTION_NONE
            return
        else:
            if self.__action == HintCustom.__ACTION_SHOW:
                if self._state == HintBase.STATE_DEFAULT:
                    self.__action = HintCustom.__ACTION_NONE
                    self._state = HintBase.STATE_HINT
                    return HINT_COMMAND.SHOW
            elif self.__action == HintCustom.__ACTION_HIDE:
                if self._state == HintBase.STATE_HINT or self._state == HintBase.STATE_COMPLETE:
                    self.__action = HintCustom.__ACTION_NONE
                    self._state = HintBase.STATE_DEFAULT
                    return HINT_COMMAND.HIDE
            elif self.__action == HintCustom.__ACTION_COMPLETE:
                self.__action = HintCustom.__ACTION_NONE
                self._state = HintBase.STATE_COMPLETE
                return HINT_COMMAND.SHOW_COMPLETED
            return

    def isActive(self):
        return self.__action == HintCustom.__ACTION_SHOW or self._state == HintBase.STATE_HINT

    def isComplete(self):
        return self._state == HintBase.STATE_COMPLETE