# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/hints/HintsBase.py


class HINT_COMMAND(object):
    SHOW = 0
    SHOW_COMPLETED = 1
    HIDE = 3


class HintBase(object):
    STATE_INACTIVE = 0
    STATE_DEFAULT = 1
    STATE_HINT = 2
    STATE_COMPLETE = 3

    def __init__(self, avatar, hintTypeId, timeout):
        super(HintBase, self).__init__()
        self._avatar = avatar
        self._timeStart = 0
        self._timeout = timeout
        self.__message = ''
        self.__voiceover = None
        self._state = HintBase.STATE_INACTIVE
        self.typeId = hintTypeId
        self.timeCompleted = 3.0
        self.cooldownAfter = 3.0
        return

    def start(self):
        pass

    def stop(self):
        pass

    def destroy(self):
        self._avatar = None
        return

    def update(self):
        return

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message):
        self.__message = message

    @property
    def voiceover(self):
        return self.__voiceover

    @voiceover.setter
    def voiceover(self, voiceover):
        self.__voiceover = voiceover