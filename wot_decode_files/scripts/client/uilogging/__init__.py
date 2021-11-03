# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/__init__.py


def getUILoggingConfig(manager):
    from uilogging.core.integration import UILoggingListener
    from uilogging.core.logger import UILoggingCore
    from skeletons.ui_logging import IUILoggingCore, IUILoggingListener
    uiLoggingCore = UILoggingCore()
    uiLoggingCore.init()
    manager.addInstance(IUILoggingCore, uiLoggingCore, finalizer='fini')
    listener = UILoggingListener()
    manager.addInstance(IUILoggingListener, listener, finalizer='fini')