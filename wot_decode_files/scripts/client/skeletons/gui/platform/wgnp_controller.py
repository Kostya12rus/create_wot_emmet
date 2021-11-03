# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/platform/wgnp_controller.py
import typing
if typing.TYPE_CHECKING:
    from Event import SafeEvent

class IWGNPRequestController(object):
    onEmailConfirmed = None
    onEmailAdded = None
    onEmailAddNeeded = None

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def addEmail(self, email, showWaiting=False):
        raise NotImplementedError

    def getEmailStatus(self, showWaiting=False):
        raise NotImplementedError

    def confirmEmail(self, code, showWaiting=False):
        raise NotImplementedError

    @property
    def emailAddedTime(self):
        raise NotImplementedError