# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/__init__.py


class prbDispatcherProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getDispatcher()


class prbEntityProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        dispatcher = g_prbLoader.getDispatcher()
        entity = None
        if dispatcher is not None:
            entity = dispatcher.getEntity()
        return entity


class prbPeripheriesHandlerProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getPeripheriesHandler()


class prbInvitesProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getInvitesManager()


class prbAutoInvitesProperty(property):

    def __get__(self, obj, objType=None):
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getAutoInvitesNotifier()