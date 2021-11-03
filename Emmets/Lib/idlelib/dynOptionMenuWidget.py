# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/dynOptionMenuWidget.py
from Tkinter import OptionMenu
from Tkinter import _setit
import copy

class DynOptionMenu(OptionMenu):

    def __init__(self, master, variable, value, *values, **kwargs):
        kwargsCopy = copy.copy(kwargs)
        if 'highlightthickness' in kwargs.keys():
            del kwargs['highlightthickness']
        OptionMenu.__init__(self, master, variable, value, *values, **kwargs)
        self.config(highlightthickness=kwargsCopy.get('highlightthickness'))
        self.variable = variable
        self.command = kwargs.get('command')

    def SetMenu(self, valueList, value=None):
        self['menu'].delete(0, 'end')
        for item in valueList:
            self['menu'].add_command(label=item, command=_setit(self.variable, item, self.command))

        if value:
            self.variable.set(value)