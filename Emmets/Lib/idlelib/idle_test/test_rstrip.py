# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_rstrip.py
import unittest, idlelib.RstripExtension as rs
from idlelib.idle_test.mock_idle import Editor

class rstripTest(unittest.TestCase):

    def test_rstrip_line(self):
        editor = Editor()
        text = editor.text
        do_rstrip = rs.RstripExtension(editor).do_rstrip
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), '')
        text.insert('1.0', '     ')
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), '')
        text.insert('1.0', '     \n')
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), '\n')

    def test_rstrip_multiple(self):
        editor = Editor()
        text = editor.text
        do_rstrip = rs.RstripExtension(editor).do_rstrip
        original = 'Line with an ending tab    \nLine ending in 5 spaces     \nLinewithnospaces\n    indented line\n    indented line with trailing space \n    '
        stripped = 'Line with an ending tab\nLine ending in 5 spaces\nLinewithnospaces\n    indented line\n    indented line with trailing space\n'
        text.insert('1.0', original)
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), stripped)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)