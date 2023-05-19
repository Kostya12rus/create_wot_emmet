# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/HealthComponent.py
import BigWorld
from Event import Event
from cgf_components_common.state_components import HealthComponent as HealthComponentCGF

class HealthComponent(BigWorld.DynamicScriptComponent, HealthComponentCGF):

    def __init__(self):
        super(HealthComponent, self).__init__()
        self.onHealthChanged = Event()

    def set_health(self, oldHealth):
        self.onHealthChanged(oldHealth, self.health, self.maxHealth)