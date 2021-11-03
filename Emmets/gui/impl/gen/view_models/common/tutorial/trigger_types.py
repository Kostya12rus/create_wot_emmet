# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/tutorial/trigger_types.py
from frameworks.wulf import ViewModel

class TriggerTypes(ViewModel):
    __slots__ = ()
    CLICK_TYPE = 'click'
    CLICK_OUTSIDE_TYPE = 'clickOutside'
    ESCAPE = 'escape'
    ENABLED = 'enabled'
    DISABLED = 'disabled'
    ENABLED_CHANGE = 'enabled_change'
    VISIBLE_CHANGE = 'visible_change'

    def __init__(self, properties=0, commands=0):
        super(TriggerTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TriggerTypes, self)._initialize()