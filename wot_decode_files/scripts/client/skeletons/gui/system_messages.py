# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/system_messages.py


class ISystemMessages(object):

    def init(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    @property
    def proto(self):
        raise NotImplementedError

    def pushMessage(self, text, type, priority=None, messageData=None, savedData=None):
        raise NotImplementedError

    def pushI18nMessage(self, key, *args, **kwargs):
        raise NotImplementedError