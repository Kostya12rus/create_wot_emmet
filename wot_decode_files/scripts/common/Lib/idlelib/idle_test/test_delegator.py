# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_delegator.py
import unittest
from idlelib.Delegator import Delegator

class DelegatorTest(unittest.TestCase):

    def test_mydel(self):
        mydel = Delegator(int)
        self.assertIs(mydel.delegate, int)
        self.assertEqual(mydel._Delegator__cache, set())
        self.assertRaises(AttributeError, mydel.__getattr__, 'xyz')
        bl = mydel.bit_length
        self.assertIs(bl, int.bit_length)
        self.assertIs(mydel.__dict__['bit_length'], int.bit_length)
        self.assertEqual(mydel._Delegator__cache, {'bit_length'})
        mydel.numerator
        self.assertEqual(mydel._Delegator__cache, {'bit_length', 'numerator'})
        del mydel.numerator
        self.assertNotIn('numerator', mydel.__dict__)
        self.assertIn('numerator', mydel._Delegator__cache)
        mydel.setdelegate(float)
        self.assertIs(mydel.delegate, float)
        self.assertNotIn('bit_length', mydel.__dict__)
        self.assertEqual(mydel._Delegator__cache, set())


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=2)