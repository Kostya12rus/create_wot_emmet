# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/sqlite3/test/py25tests.py
from __future__ import with_statement
import unittest, sqlite3 as sqlite
did_rollback = False

class MyConnection(sqlite.Connection):

    def rollback(self):
        global did_rollback
        did_rollback = True
        sqlite.Connection.rollback(self)


class ContextTests(unittest.TestCase):

    def setUp(self):
        global did_rollback
        self.con = sqlite.connect(':memory:', factory=MyConnection)
        self.con.execute('create table test(c unique)')
        did_rollback = False

    def tearDown(self):
        self.con.close()

    def CheckContextManager(self):
        with self.con:
            pass

    def CheckContextManagerCommit(self):
        with self.con:
            self.con.execute("insert into test(c) values ('foo')")
        self.con.rollback()
        count = self.con.execute('select count(*) from test').fetchone()[0]
        self.assertEqual(count, 1)

    def CheckContextManagerRollback(self):
        self.assertEqual(did_rollback, False)
        try:
            with self.con:
                self.con.execute('insert into test(c) values (4)')
                self.con.execute('insert into test(c) values (4)')
        except sqlite.IntegrityError:
            pass

        self.assertEqual(did_rollback, True)


def suite():
    ctx_suite = unittest.makeSuite(ContextTests, 'Check')
    return unittest.TestSuite((ctx_suite,))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())


if __name__ == '__main__':
    test()