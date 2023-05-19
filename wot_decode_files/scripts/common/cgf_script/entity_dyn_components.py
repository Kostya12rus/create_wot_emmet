# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_script/entity_dyn_components.py


class BWEntitiyComponentTracker(object):

    def onDynamicComponentCreated(self, component):
        existing = self.entityGameObject.findComponentByType(type(component))
        if existing is None:
            self.entityGameObject.addComponent(component)
        supMethod = getattr(super(BWEntitiyComponentTracker, self), 'onDynamicComponentCreated', None)
        if supMethod is not None:
            supMethod(self, component)
        return

    def onDynamicComponentDestroyed(self, component):
        existing = self.entityGameObject.findComponentByType(type(component))
        if existing is component:
            self.entityGameObject.removeComponent(component)
        supMethod = getattr(super(BWEntitiyComponentTracker, self), 'onDynamicComponentDestroyed', None)
        if supMethod is not None:
            supMethod(self, component)
        return