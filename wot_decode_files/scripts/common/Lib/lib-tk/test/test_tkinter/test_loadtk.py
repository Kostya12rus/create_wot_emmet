# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/test/test_tkinter/test_loadtk.py
import os, sys, unittest
from test import test_support
from Tkinter import Tcl, TclError
test_support.requires('gui')

class TkLoadTest(unittest.TestCase):

    @unittest.skipIf('DISPLAY' not in os.environ, 'No $DISPLAY set.')
    def testLoadTk(self):
        tcl = Tcl()
        self.assertRaises(TclError, tcl.winfo_geometry)
        tcl.loadtk()
        self.assertEqual('1x1+0+0', tcl.winfo_geometry())
        tcl.destroy()

    def testLoadTkFailure(self):
        old_display = None
        if sys.platform.startswith(('win', 'darwin', 'cygwin')):
            return
        else:
            with test_support.EnvironmentVarGuard() as (env):
                if 'DISPLAY' in os.environ:
                    del env['DISPLAY']
                    display = os.popen('echo $DISPLAY').read().strip()
                    if display:
                        return
                tcl = Tcl()
                self.assertRaises(TclError, tcl.winfo_geometry)
                self.assertRaises(TclError, tcl.loadtk)
            return


tests_gui = (
 TkLoadTest,)
if __name__ == '__main__':
    test_support.run_unittest(*tests_gui)