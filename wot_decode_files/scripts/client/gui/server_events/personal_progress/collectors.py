# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/personal_progress/collectors.py
import typing, quest_progress
from constants import QUEST_PROGRESS_STATE
from personal_missions_constants import VISIBLE_SCOPE, CONTAINER

class ClientProgressCollector(quest_progress.IDataCollector):

    @classmethod
    def validate(cls, progress):
        return bool(progress.getVisibleScope())

    @classmethod
    def collect(cls, progress):
        return progress


class HeaderProgressCollector(ClientProgressCollector):

    @classmethod
    def validate(cls, progress):
        return progress.getContainerType() == CONTAINER.HEADER


class BodyProgressCollector(ClientProgressCollector):

    @classmethod
    def validate(cls, progress):
        return progress.getContainerType() == CONTAINER.BODY


class LobbyProgressCollector(ClientProgressCollector):

    @classmethod
    def validate(cls, progress):
        return VISIBLE_SCOPE.HANGAR in progress.getVisibleScope()


class BattleProgressCollector(ClientProgressCollector):

    @classmethod
    def validate(cls, progress):
        return VISIBLE_SCOPE.BATTLE in progress.getVisibleScope()


class SubQuestProgressCollector(ClientProgressCollector):
    __slots__ = ('_isMain', )

    def __init__(self, isMain=None):
        self._isMain = isMain

    def validate(self, progress):
        if self._isMain is not None:
            if progress.isMain() == self._isMain:
                return super(SubQuestProgressCollector, self).validate(progress)
            return False
        return True


class LobbyHeaderProgressCollector(SubQuestProgressCollector):

    def validate(self, progress):
        result = super(LobbyHeaderProgressCollector, self).validate(progress)
        return result and LobbyProgressCollector.validate(progress) and HeaderProgressCollector.validate(progress)


class LobbyBodyProgressCollector(SubQuestProgressCollector):

    def validate(self, progress):
        result = super(LobbyBodyProgressCollector, self).validate(progress)
        return result and LobbyProgressCollector.validate(progress) and BodyProgressCollector.validate(progress)


class BattleHeaderProgressCollector(SubQuestProgressCollector):

    def validate(self, progress):
        result = super(BattleHeaderProgressCollector, self).validate(progress)
        return result and BattleProgressCollector.validate(progress) and HeaderProgressCollector.validate(progress)


class BattleBodyProgressCollector(SubQuestProgressCollector):

    def validate(self, progress):
        result = super(BattleBodyProgressCollector, self).validate(progress)
        return result and BattleProgressCollector.validate(progress) and BodyProgressCollector.validate(progress)


class ChangedProgressCollector(BattleBodyProgressCollector):

    def validate(self, condProgress):
        if condProgress.isChanged():
            return super(ChangedProgressCollector, self).validate(condProgress)
        return False


class ProgressWithTimerCollector(BattleBodyProgressCollector):

    def validate(self, condProgress):
        result = super(ProgressWithTimerCollector, self).validate(condProgress)
        if result:
            return condProgress.getCountDown() is not None and condProgress.getState() not in (QUEST_PROGRESS_STATE.COMPLETED, QUEST_PROGRESS_STATE.FAILED)
        else:
            return False