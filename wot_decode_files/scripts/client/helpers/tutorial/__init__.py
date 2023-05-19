# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/tutorial/__init__.py
from helpers.tutorial.stubs import StubTutorialLoader
from skeletons.tutorial import ITutorialLoader

def getTutorialConfig(manager):
    manager.addInstance(ITutorialLoader, StubTutorialLoader(), finalizer='fini')