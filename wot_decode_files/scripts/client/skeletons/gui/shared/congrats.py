# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/skeletons/gui/shared/congrats.py


class ICongratsCtx(object):

    @property
    def background(self):
        raise NotImplementedError

    @property
    def title(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def image(self):
        raise NotImplementedError

    @property
    def imageAlt(self):
        raise NotImplementedError

    @property
    def confirmLabel(self):
        raise NotImplementedError

    @property
    def backLabel(self):
        raise NotImplementedError

    def onConfirm(self):
        raise NotImplementedError

    def onBack(self):
        raise NotImplementedError