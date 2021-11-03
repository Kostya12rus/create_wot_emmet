# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/core_constants.py


class SettingsStatuses(object):
    REQUESTED = 'requested'
    ENABLED = 'enabled'
    DISABLED = 'disabled'


class LogLevels(object):
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30


HTTP_OK_STATUS = 200
HTTP_DEFAULT_TIMEOUT = 5
HTTP_DEFAULT_HEADERS = {'Content-Type': 'application/json'}