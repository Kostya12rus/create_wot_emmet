# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/new_year/__init__.py
from skeletons.festivity_factory import IFestivityFactory
from skeletons.new_year import ICustomizableObjectsManager

def getNewYearServiceConfig(manager):
    from .customizable_objects_manager import CustomizableObjectsManager
    from new_year.ny_factory import NewYearFactory
    custObjMgr = CustomizableObjectsManager()
    custObjMgr.init()
    manager.addInstance(ICustomizableObjectsManager, custObjMgr, finalizer='fini')
    manager.addInstance(IFestivityFactory, NewYearFactory())