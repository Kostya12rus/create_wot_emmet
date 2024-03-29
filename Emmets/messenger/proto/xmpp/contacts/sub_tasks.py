# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/contacts/sub_tasks.py
from messenger.m_constants import USER_TAG, USER_ACTION_ID, CLIENT_ACTION_ID
from messenger.proto.xmpp import errors
from messenger.proto.xmpp.contacts.roster_tasks import SyncSubscriptionTask
from messenger.proto.xmpp.contacts.tasks import TaskResult
from messenger.proto.xmpp.gloox_constants import SUBSCRIPTION as _SUB

class AskSubscriptionTask(SyncSubscriptionTask):

    def sync(self, name, groups, sub=None, clanInfo=None):
        if sub[0] != _SUB.OFF:
            self._result = TaskResult.REMOVE
        self._doSync(name, groups, sub, clanInfo)
        return self._result

    def _doRun(self, client):
        client.askSubscription(self._jid)

    def _getError(self, pyGlooxTag):
        return errors.createServerActionIQError(CLIENT_ACTION_ID.RQ_FRIENDSHIP, pyGlooxTag)


class _ChangeSubscriptionTask(SyncSubscriptionTask):
    __slots__ = ('_auto', )

    def __init__(self, jid, name='', auto=False):
        super(_ChangeSubscriptionTask, self).__init__(jid, name)
        self._auto = auto


class ApproveSubscriptionTask(_ChangeSubscriptionTask):
    __slots__ = ('_tasks', )

    def __init__(self, jid, name='', auto=False):
        super(ApproveSubscriptionTask, self).__init__(jid, name, auto)
        self._tasks = []

    def clone(self):
        return self._tasks

    def sync(self, name, groups, sub=None, clanInfo=None):
        if sub is not None and sub[1] == _SUB.ON:
            user = self._getUser()
            self._result = TaskResult.REMOVE
            if user and not self._auto:
                user.removeTags({USER_TAG.SUB_IN_PROCESS})
                user.addTags({USER_TAG.SUB_APPROVED})
            if self._auto and sub[0] == _SUB.PENDING:
                self._tasks.append(AskSubscriptionTask(self._jid))
                self._result |= TaskResult.CLONE
        self._doSync(name, groups, sub, clanInfo)
        return self._result

    def _doRun(self, client):
        user = self._getUser()
        if user:
            user.addTags({USER_TAG.SUB_IN_PROCESS})
            self._doNotify(USER_ACTION_ID.SUBSCRIPTION_CHANGED, user, nextRev=False)
        client.approveSubscription(self._jid)

    def _getError(self, pyGlooxTag):
        return errors.createServerActionIQError(CLIENT_ACTION_ID.APPROVE_FRIENDSHIP, pyGlooxTag)


class CancelSubscriptionTask(_ChangeSubscriptionTask):

    def isInstantaneous(self):
        return True

    def _doRun(self, client):
        user = self._getUser()
        if user:
            user.update(item=None)
            if not self._auto:
                user.addTags({USER_TAG.SUB_CANCELED})
                self._doNotify(USER_ACTION_ID.SUBSCRIPTION_CHANGED, user, nextRev=False)
        client.cancelSubscription(self._jid)
        return