# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/__init__.py
from skeletons.gui.web import IWebController
__all__ = ('getWebServicesConfig', )

def getWebServicesConfig(manager):
    from gui.wgcg.web_controller import WebController
    ctrl = WebController()
    ctrl.init()
    manager.addInstance(IWebController, ctrl, finalizer='fini')