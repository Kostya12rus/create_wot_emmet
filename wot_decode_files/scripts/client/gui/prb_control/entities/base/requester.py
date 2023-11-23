# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/requester.py


class IPrbListRequester(object):

    def start(self, callback):
        pass

    def stop(self):
        pass

    def request(self, ctx=None):
        pass


class IUnitRequestProcessor(object):

    def init(self):
        pass

    def fini(self):
        pass

    def doRequest(self, ctx, methodName, *args, **kwargs):
        pass

    def doRequestChain(self, ctx, chain):
        pass

    def doRawRequest(self, methodName, *args, **kwargs):
        pass