# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/test/test_tkinter/test_text.py
import unittest, Tkinter
from test.test_support import requires, run_unittest
from ttk import setup_master
requires('gui')

class TextTest(unittest.TestCase):

    def setUp(self):
        self.root = setup_master()
        self.text = Tkinter.Text(self.root)

    def tearDown(self):
        self.text.destroy()

    def test_debug(self):
        text = self.text
        olddebug = text.debug()
        try:
            text.debug(0)
            self.assertEqual(text.debug(), 0)
            text.debug(1)
            self.assertEqual(text.debug(), 1)
        finally:
            text.debug(olddebug)
            self.assertEqual(text.debug(), olddebug)

    def test_search(self):
        text = self.text
        self.assertRaises(Tkinter.TclError, text.search, None, '1.0')
        self.assertRaises(Tkinter.TclError, text.search, 'a', None)
        self.assertRaises(Tkinter.TclError, text.search, None, None)
        self.assertRaises(Tkinter.TclError, text.search, '', 0)
        text.insert('1.0', 'hi-test')
        self.assertEqual(text.search('-test', '1.0', 'end'), '1.2')
        self.assertEqual(text.search('test', '1.0', 'end'), '1.3')
        return


tests_gui = (
 TextTest,)
if __name__ == '__main__':
    run_unittest(*tests_gui)