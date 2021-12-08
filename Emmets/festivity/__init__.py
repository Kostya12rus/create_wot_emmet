# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/festivity/__init__.py
from skeletons.festivity_factory import IFestivityFactory
from skeletons.new_year import INewYearController, ICustomizableObjectsManager

def getFestivityConfig(manager):
    from new_year.customizable_objects_manager import CustomizableObjectsManager
    from new_year.ny_factory import NewYearFactory
    festivityFactory = NewYearFactory()
    manager.addInstance(IFestivityFactory, festivityFactory)

    def _create():
        customizableObjMgr = CustomizableObjectsManager()
        customizableObjMgr.init()
        return customizableObjMgr

    manager.addRuntime(ICustomizableObjectsManager, _create, finalizer='fini')
    manager.addInstance(INewYearController, festivityFactory.getController())