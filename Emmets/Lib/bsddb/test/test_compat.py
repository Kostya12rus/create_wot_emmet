# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/bsddb/test/test_compat.py
import os, string, unittest
from test_all import db, hashopen, btopen, rnopen, verbose, get_new_database_path

class CompatibilityTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = get_new_database_path()

    def tearDown(self):
        try:
            os.remove(self.filename)
        except os.error:
            pass

    def test01_btopen(self):
        self.do_bthash_test(btopen, 'btopen')

    def test02_hashopen(self):
        self.do_bthash_test(hashopen, 'hashopen')

    def test03_rnopen(self):
        data = ('The quick brown fox jumped over the lazy dog.').split()
        if verbose:
            print '\nTesting: rnopen'
        f = rnopen(self.filename, 'c')
        for x in range(len(data)):
            f[x + 1] = data[x]

        getTest = (f[1], f[2], f[3])
        if verbose:
            print '%s %s %s' % getTest
        self.assertEqual(getTest[1], 'quick', 'data mismatch!')
        rv = f.set_location(3)
        if rv != (3, 'brown'):
            self.fail('recno database set_location failed: ' + repr(rv))
        f[25] = 'twenty-five'
        f.close()
        del f
        f = rnopen(self.filename, 'w')
        f[20] = 'twenty'

        def noRec(f):
            rec = f[15]

        self.assertRaises(KeyError, noRec, f)

        def badKey(f):
            rec = f['a string']

        self.assertRaises(TypeError, badKey, f)
        del f[3]
        rec = f.first()
        while rec:
            if verbose:
                print rec
            try:
                rec = f.next()
            except KeyError:
                break

        f.close()

    def test04_n_flag(self):
        f = hashopen(self.filename, 'n')
        f.close()

    def do_bthash_test(self, factory, what):
        if verbose:
            print '\nTesting: ', what
        f = factory(self.filename, 'c')
        if verbose:
            print 'creation...'
        if f:
            if verbose:
                print 'truth test: true'
        else:
            if verbose:
                print 'truth test: false'
            f['0'] = ''
            f['a'] = 'Guido'
            f['b'] = 'van'
            f['c'] = 'Rossum'
            f['d'] = 'invented'
            f['f'] = 'Python'
            if verbose:
                print '%s %s %s' % (f['a'], f['b'], f['c'])
            if verbose:
                print 'key ordering...'
            start = f.set_location(f.first()[0])
            if start != ('0', ''):
                self.fail('incorrect first() result: ' + repr(start))
            while 1:
                try:
                    rec = f.next()
                except KeyError:
                    self.assertEqual(rec, f.last(), 'Error, last <> last!')
                    f.previous()
                    break

                if verbose:
                    print rec

            self.assertTrue(f.has_key('f'), 'Error, missing key!')
            if factory == btopen:
                e = f.set_location('e')
                if e != ('f', 'Python'):
                    self.fail('wrong key,value returned: ' + repr(e))
            else:
                try:
                    e = f.set_location('e')
                except KeyError:
                    pass
                else:
                    self.fail('set_location on non-existent key did not raise KeyError')

            f.sync()
            f.close()
            try:
                if f:
                    if verbose:
                        print 'truth test: true'
                elif verbose:
                    print 'truth test: false'
            except db.DBError:
                pass
            else:
                self.fail('Exception expected')

            del f
            if verbose:
                print 'modification...'
            f = factory(self.filename, 'w')
            f['d'] = 'discovered'
            if verbose:
                print 'access...'
            for key in f.keys():
                word = f[key]
                if verbose:
                    print word

        def noRec(f):
            rec = f['no such key']

        self.assertRaises(KeyError, noRec, f)

        def badKey(f):
            rec = f[15]

        self.assertRaises(TypeError, badKey, f)
        f.close()


def test_suite():
    return unittest.makeSuite(CompatibilityTestCase)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')