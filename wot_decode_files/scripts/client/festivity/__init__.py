# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/__init__.py
from festivity.dummy.df_factory import DummyFactory
from skeletons.festivity_factory import IFestivityFactory

def getFestivityConfig(manager):
    festivityFactory = DummyFactory()
    manager.addInstance(IFestivityFactory, festivityFactory)