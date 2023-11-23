# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/tkColorChooser.py
from tkCommonDialog import Dialog

class Chooser(Dialog):
    command = 'tk_chooseColor'

    def _fixoptions(self):
        try:
            color = self.options['initialcolor']
            if isinstance(color, tuple):
                self.options['initialcolor'] = '#%02x%02x%02x' % color
        except KeyError:
            pass

    def _fixresult(self, widget, result):
        if not result or not str(result):
            return (None, None)
        r, g, b = widget.winfo_rgb(result)
        return ((r / 256, g / 256, b / 256), str(result))


def askcolor(color=None, **options):
    if color:
        options = options.copy()
        options['initialcolor'] = color
    return Chooser(**options).show()


if __name__ == '__main__':
    print 'color', askcolor()