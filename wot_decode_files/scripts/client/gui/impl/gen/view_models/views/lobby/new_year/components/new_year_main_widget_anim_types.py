# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/new_year/components/new_year_main_widget_anim_types.py
from frameworks.wulf import ViewModel

class NewYearMainWidgetAnimTypes(ViewModel):
    __slots__ = ()
    ANIM_TYPE_NONE = 'none'
    ANIM_TYPE_UP_LONG = 'upLong'

    def __init__(self, properties=0, commands=0):
        super(NewYearMainWidgetAnimTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(NewYearMainWidgetAnimTypes, self)._initialize()