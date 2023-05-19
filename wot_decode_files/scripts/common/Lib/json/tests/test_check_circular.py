# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/json/tests/test_check_circular.py
from json.tests import PyTest, CTest

def default_iterable(obj):
    return list(obj)


class TestCheckCircular(object):

    def test_circular_dict(self):
        dct = {}
        dct['a'] = dct
        self.assertRaises(ValueError, self.dumps, dct)

    def test_circular_list(self):
        lst = []
        lst.append(lst)
        self.assertRaises(ValueError, self.dumps, lst)

    def test_circular_composite(self):
        dct2 = {}
        dct2['a'] = []
        dct2['a'].append(dct2)
        self.assertRaises(ValueError, self.dumps, dct2)

    def test_circular_default(self):
        self.dumps([set()], default=default_iterable)
        self.assertRaises(TypeError, self.dumps, [set()])

    def test_circular_off_default(self):
        self.dumps([set()], default=default_iterable, check_circular=False)
        self.assertRaises(TypeError, self.dumps, [set()], check_circular=False)


class TestPyCheckCircular(TestCheckCircular, PyTest):
    pass


class TestCCheckCircular(TestCheckCircular, CTest):
    pass