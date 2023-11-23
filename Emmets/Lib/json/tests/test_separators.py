# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/json/tests/test_separators.py
import textwrap
from json.tests import PyTest, CTest

class TestSeparators(object):

    def test_separators(self):
        h = [
         [
          'blorpie'], ['whoops'], [], 'd-shtaeou', 'd-nthiouh', 'i-vhbjkhnth', {'nifty': 87}, {'field': 'yes', 'morefield': False}]
        expect = textwrap.dedent('        [\n          [\n            "blorpie"\n          ] ,\n          [\n            "whoops"\n          ] ,\n          [] ,\n          "d-shtaeou" ,\n          "d-nthiouh" ,\n          "i-vhbjkhnth" ,\n          {\n            "nifty" : 87\n          } ,\n          {\n            "field" : "yes" ,\n            "morefield" : false\n          }\n        ]')
        d1 = self.dumps(h)
        d2 = self.dumps(h, indent=2, sort_keys=True, separators=(' ,', ' : '))
        h1 = self.loads(d1)
        h2 = self.loads(d2)
        self.assertEqual(h1, h)
        self.assertEqual(h2, h)
        self.assertEqual(d2, expect)


class TestPySeparators(TestSeparators, PyTest):
    pass


class TestCSeparators(TestSeparators, CTest):
    pass