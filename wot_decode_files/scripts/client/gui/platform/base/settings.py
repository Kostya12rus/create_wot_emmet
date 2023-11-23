# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/base/settings.py
import httplib
REQUEST_TIMEOUT = 30.0
POLLING_PERIOD = 1.0
POLLING_REQUEST_TIMEOUT = 15.0
SOLVE_POW_TIMEOUT = 15.0
CONTENT_WAITING = 'loadContent'
ACCEPTED_HTTP_CODES = (
 httplib.OK, httplib.CREATED)