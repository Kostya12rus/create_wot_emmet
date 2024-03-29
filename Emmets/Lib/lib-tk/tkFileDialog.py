# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/tkFileDialog.py
from tkCommonDialog import Dialog

class _Dialog(Dialog):

    def _fixoptions(self):
        try:
            self.options['filetypes'] = tuple(self.options['filetypes'])
        except KeyError:
            pass

    def _fixresult(self, widget, result):
        if result:
            import os
            try:
                result = result.string
            except AttributeError:
                pass

            path, file = os.path.split(result)
            self.options['initialdir'] = path
            self.options['initialfile'] = file
        self.filename = result
        return result


class Open(_Dialog):
    command = 'tk_getOpenFile'

    def _fixresult(self, widget, result):
        if isinstance(result, tuple):
            result = tuple([ getattr(r, 'string', r) for r in result ])
            if result:
                import os
                path, file = os.path.split(result[0])
                self.options['initialdir'] = path
            return result
        if not widget.tk.wantobjects() and 'multiple' in self.options:
            return self._fixresult(widget, widget.tk.splitlist(result))
        return _Dialog._fixresult(self, widget, result)


class SaveAs(_Dialog):
    command = 'tk_getSaveFile'


class Directory(Dialog):
    command = 'tk_chooseDirectory'

    def _fixresult(self, widget, result):
        if result:
            try:
                result = result.string
            except AttributeError:
                pass

            self.options['initialdir'] = result
        self.directory = result
        return result


def askopenfilename(**options):
    return Open(**options).show()


def asksaveasfilename(**options):
    return SaveAs(**options).show()


def askopenfilenames(**options):
    options['multiple'] = 1
    return Open(**options).show()


def askopenfile(mode='r', **options):
    filename = Open(**options).show()
    if filename:
        return open(filename, mode)
    else:
        return


def askopenfiles(mode='r', **options):
    files = askopenfilenames(**options)
    if files:
        ofiles = []
        for filename in files:
            ofiles.append(open(filename, mode))

        files = ofiles
    return files


def asksaveasfile(mode='w', **options):
    filename = SaveAs(**options).show()
    if filename:
        return open(filename, mode)
    else:
        return


def askdirectory(**options):
    return Directory(**options).show()


if __name__ == '__main__':
    enc = 'utf-8'
    import sys
    try:
        import locale
        locale.setlocale(locale.LC_ALL, '')
        enc = locale.nl_langinfo(locale.CODESET)
    except (ImportError, AttributeError):
        pass

    openfilename = askopenfilename(filetypes=[('all files', '*')])
    try:
        fp = open(openfilename, 'r')
        fp.close()
    except:
        print 'Could not open File: '
        print sys.exc_info()[1]

    print 'open', openfilename.encode(enc)
    saveasfilename = asksaveasfilename()
    print 'saveas', saveasfilename.encode(enc)