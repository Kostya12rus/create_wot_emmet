# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/Dialog.py
from Tkinter import *
from Tkinter import _cnfmerge
if TkVersion <= 3.6:
    DIALOG_ICON = 'warning'
else:
    DIALOG_ICON = 'questhead'

class Dialog(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        self.widgetName = '__dialog__'
        Widget._setup(self, master, cnf)
        self.num = self.tk.getint(self.tk.call('tk_dialog', self._w, cnf['title'], cnf['text'], cnf['bitmap'], cnf['default'], *cnf['strings']))
        try:
            Widget.destroy(self)
        except TclError:
            pass

    def destroy(self):
        pass


def _test():
    d = Dialog(None, {'title': 'File Modified', 'text': 'File "Python.h" has been modified since the last time it was saved. Do you want to save it before exiting the application.', 
       'bitmap': DIALOG_ICON, 
       'default': 0, 
       'strings': ('Save File', 'Discard Changes', 'Return to Editor')})
    print d.num
    return


if __name__ == '__main__':
    t = Button(None, {'text': 'Test', 'command': _test, 
       Pack: {}})
    q = Button(None, {'text': 'Quit', 'command': t.quit, 
       Pack: {}})
    t.mainloop()