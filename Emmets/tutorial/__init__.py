# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/__init__.py
from __future__ import absolute_import
from skeletons.tutorial import ITutorialLoader

def getTutorialConfig(manager):
    from tutorial.loader import TutorialLoader
    loader = TutorialLoader()
    loader.init()
    manager.addInstance(ITutorialLoader, loader, finalizer='fini')