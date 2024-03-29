# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/bsddb/test/test_compare.py
import sys, os, re, test_all
from cStringIO import StringIO
import unittest
from test_all import db, dbshelve, test_support, get_new_environment_path, get_new_database_path

def cmp(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    return 1


lexical_cmp = cmp

def lowercase_cmp(left, right):
    return cmp(left.lower(), right.lower())


def make_reverse_comparator(cmp):

    def reverse(left, right, delegate=cmp):
        return -delegate(left, right)

    return reverse


_expected_lexical_test_data = [
 '', 'CCCP', 'a', 'aaa', 'b', 'c', 'cccce', 'ccccf']
_expected_lowercase_test_data = ['', 'a', 'aaa', 'b', 'c', 'CC', 'cccce', 'ccccf', 'CCCP']

class ComparatorTests(unittest.TestCase):

    def comparator_test_helper(self, comparator, expected_data):
        data = expected_data[:]
        import sys
        if sys.version_info < (2, 6):
            data.sort(cmp=comparator)
        else:
            data2 = []
            for i in data:
                for j, k in enumerate(data2):
                    r = comparator(k, i)
                    if r == 1:
                        data2.insert(j, i)
                        break
                else:
                    data2.append(i)

            data = data2
        self.assertEqual(data, expected_data, "comparator `%s' is not right: %s vs. %s" % (
         comparator, expected_data, data))

    def test_lexical_comparator(self):
        self.comparator_test_helper(lexical_cmp, _expected_lexical_test_data)

    def test_reverse_lexical_comparator(self):
        rev = _expected_lexical_test_data[:]
        rev.reverse()
        self.comparator_test_helper(make_reverse_comparator(lexical_cmp), rev)

    def test_lowercase_comparator(self):
        self.comparator_test_helper(lowercase_cmp, _expected_lowercase_test_data)


class AbstractBtreeKeyCompareTestCase(unittest.TestCase):
    env = None
    db = None
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3,
                                                                                       2):

        def assertLess(self, a, b, msg=None):
            return self.assertTrue(a < b, msg=msg)

    def setUp(self):
        self.filename = self.__class__.__name__ + '.db'
        self.homeDir = get_new_environment_path()
        env = db.DBEnv()
        env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_THREAD)
        self.env = env

    def tearDown(self):
        self.closeDB()
        if self.env is not None:
            self.env.close()
            self.env = None
        test_support.rmtree(self.homeDir)
        return

    def addDataToDB(self, data):
        i = 0
        for item in data:
            self.db.put(item, str(i))
            i = i + 1

    def createDB(self, key_comparator):
        self.db = db.DB(self.env)
        self.setupDB(key_comparator)
        self.db.open(self.filename, 'test', db.DB_BTREE, db.DB_CREATE)

    def setupDB(self, key_comparator):
        self.db.set_bt_compare(key_comparator)

    def closeDB(self):
        if self.db is not None:
            self.db.close()
            self.db = None
        return

    def startTest(self):
        pass

    def finishTest(self, expected=None):
        if expected is not None:
            self.check_results(expected)
        self.closeDB()
        return

    def check_results(self, expected):
        curs = self.db.cursor()
        try:
            index = 0
            rec = curs.first()
            while rec:
                key, ignore = rec
                self.assertLess(index, len(expected), 'to many values returned from cursor')
                self.assertEqual(expected[index], key, "expected value `%s' at %d but got `%s'" % (
                 expected[index], index, key))
                index = index + 1
                rec = curs.next()

            self.assertEqual(index, len(expected), 'not enough values returned from cursor')
        finally:
            curs.close()


class BtreeKeyCompareTestCase(AbstractBtreeKeyCompareTestCase):

    def runCompareTest(self, comparator, data):
        self.startTest()
        self.createDB(comparator)
        self.addDataToDB(data)
        self.finishTest(data)

    def test_lexical_ordering(self):
        self.runCompareTest(lexical_cmp, _expected_lexical_test_data)

    def test_reverse_lexical_ordering(self):
        expected_rev_data = _expected_lexical_test_data[:]
        expected_rev_data.reverse()
        self.runCompareTest(make_reverse_comparator(lexical_cmp), expected_rev_data)

    def test_compare_function_useless(self):
        self.startTest()

        def socialist_comparator(l, r):
            return 0

        self.createDB(socialist_comparator)
        self.addDataToDB(['b', 'a', 'd'])
        self.finishTest(['b'])


class BtreeExceptionsTestCase(AbstractBtreeKeyCompareTestCase):

    def test_raises_non_callable(self):
        self.startTest()
        self.assertRaises(TypeError, self.createDB, 'abc')
        self.assertRaises(TypeError, self.createDB, None)
        self.finishTest()
        return

    def test_set_bt_compare_with_function(self):
        self.startTest()
        self.createDB(lexical_cmp)
        self.finishTest()

    def check_results(self, results):
        pass

    def test_compare_function_incorrect(self):
        self.startTest()

        def bad_comparator(l, r):
            return 1

        self.assertRaises(TypeError, self.createDB, bad_comparator)
        self.finishTest()

    def verifyStderr(self, method, successRe):
        stdErr = sys.stderr
        sys.stderr = StringIO()
        try:
            method()
        finally:
            temp = sys.stderr
            sys.stderr = stdErr
            errorOut = temp.getvalue()
            if not successRe.search(errorOut):
                self.fail('unexpected stderr output:\n' + errorOut)

        if sys.version_info < (3, 0):
            sys.exc_traceback = sys.last_traceback = None
        return

    def _test_compare_function_exception(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            raise RuntimeError, "i'm a naughty comparison function"

        self.createDB(bad_comparator)
        self.addDataToDB(['a', 'b', 'c'])
        self.finishTest()

    def test_compare_function_exception(self):
        self.verifyStderr(self._test_compare_function_exception, re.compile('(^RuntimeError:.* naughty.*){2}', re.M | re.S))

    def _test_compare_function_bad_return(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            return l

        self.createDB(bad_comparator)
        self.addDataToDB(['a', 'b', 'c'])
        self.finishTest()

    def test_compare_function_bad_return(self):
        self.verifyStderr(self._test_compare_function_bad_return, re.compile('(^TypeError:.* return an int.*){2}', re.M | re.S))

    def test_cannot_assign_twice(self):

        def my_compare(a, b):
            return 0

        self.startTest()
        self.createDB(my_compare)
        self.assertRaises(RuntimeError, self.db.set_bt_compare, my_compare)


class AbstractDuplicateCompareTestCase(unittest.TestCase):
    env = None
    db = None
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3,
                                                                                       2):

        def assertLess(self, a, b, msg=None):
            return self.assertTrue(a < b, msg=msg)

    def setUp(self):
        self.filename = self.__class__.__name__ + '.db'
        self.homeDir = get_new_environment_path()
        env = db.DBEnv()
        env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_THREAD)
        self.env = env

    def tearDown(self):
        self.closeDB()
        if self.env is not None:
            self.env.close()
            self.env = None
        test_support.rmtree(self.homeDir)
        return

    def addDataToDB(self, data):
        for item in data:
            self.db.put('key', item)

    def createDB(self, dup_comparator):
        self.db = db.DB(self.env)
        self.setupDB(dup_comparator)
        self.db.open(self.filename, 'test', db.DB_BTREE, db.DB_CREATE)

    def setupDB(self, dup_comparator):
        self.db.set_flags(db.DB_DUPSORT)
        self.db.set_dup_compare(dup_comparator)

    def closeDB(self):
        if self.db is not None:
            self.db.close()
            self.db = None
        return

    def startTest(self):
        pass

    def finishTest(self, expected=None):
        if expected is not None:
            self.check_results(expected)
        self.closeDB()
        return

    def check_results(self, expected):
        curs = self.db.cursor()
        try:
            index = 0
            rec = curs.first()
            while rec:
                ignore, data = rec
                self.assertLess(index, len(expected), 'to many values returned from cursor')
                self.assertEqual(expected[index], data, "expected value `%s' at %d but got `%s'" % (
                 expected[index], index, data))
                index = index + 1
                rec = curs.next()

            self.assertEqual(index, len(expected), 'not enough values returned from cursor')
        finally:
            curs.close()


class DuplicateCompareTestCase(AbstractDuplicateCompareTestCase):

    def runCompareTest(self, comparator, data):
        self.startTest()
        self.createDB(comparator)
        self.addDataToDB(data)
        self.finishTest(data)

    def test_lexical_ordering(self):
        self.runCompareTest(lexical_cmp, _expected_lexical_test_data)

    def test_reverse_lexical_ordering(self):
        expected_rev_data = _expected_lexical_test_data[:]
        expected_rev_data.reverse()
        self.runCompareTest(make_reverse_comparator(lexical_cmp), expected_rev_data)


class DuplicateExceptionsTestCase(AbstractDuplicateCompareTestCase):

    def test_raises_non_callable(self):
        self.startTest()
        self.assertRaises(TypeError, self.createDB, 'abc')
        self.assertRaises(TypeError, self.createDB, None)
        self.finishTest()
        return

    def test_set_dup_compare_with_function(self):
        self.startTest()
        self.createDB(lexical_cmp)
        self.finishTest()

    def check_results(self, results):
        pass

    def test_compare_function_incorrect(self):
        self.startTest()

        def bad_comparator(l, r):
            return 1

        self.assertRaises(TypeError, self.createDB, bad_comparator)
        self.finishTest()

    def test_compare_function_useless(self):
        self.startTest()

        def socialist_comparator(l, r):
            return 0

        self.createDB(socialist_comparator)
        self.assertRaises(db.DBKeyExistError, self.addDataToDB, ['b', 'a', 'd'])
        self.finishTest()

    def verifyStderr(self, method, successRe):
        stdErr = sys.stderr
        sys.stderr = StringIO()
        try:
            method()
        finally:
            temp = sys.stderr
            sys.stderr = stdErr
            errorOut = temp.getvalue()
            if not successRe.search(errorOut):
                self.fail('unexpected stderr output:\n' + errorOut)

        if sys.version_info < (3, 0):
            sys.exc_traceback = sys.last_traceback = None
        return

    def _test_compare_function_exception(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            raise RuntimeError, "i'm a naughty comparison function"

        self.createDB(bad_comparator)
        self.addDataToDB(['a', 'b', 'c'])
        self.finishTest()

    def test_compare_function_exception(self):
        self.verifyStderr(self._test_compare_function_exception, re.compile('(^RuntimeError:.* naughty.*){2}', re.M | re.S))

    def _test_compare_function_bad_return(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            return l

        self.createDB(bad_comparator)
        self.addDataToDB(['a', 'b', 'c'])
        self.finishTest()

    def test_compare_function_bad_return(self):
        self.verifyStderr(self._test_compare_function_bad_return, re.compile('(^TypeError:.* return an int.*){2}', re.M | re.S))

    def test_cannot_assign_twice(self):

        def my_compare(a, b):
            return 0

        self.startTest()
        self.createDB(my_compare)
        self.assertRaises(RuntimeError, self.db.set_dup_compare, my_compare)


def test_suite():
    res = unittest.TestSuite()
    res.addTest(unittest.makeSuite(ComparatorTests))
    res.addTest(unittest.makeSuite(BtreeExceptionsTestCase))
    res.addTest(unittest.makeSuite(BtreeKeyCompareTestCase))
    res.addTest(unittest.makeSuite(DuplicateExceptionsTestCase))
    res.addTest(unittest.makeSuite(DuplicateCompareTestCase))
    return res


if __name__ == '__main__':
    unittest.main(defaultTest='suite')