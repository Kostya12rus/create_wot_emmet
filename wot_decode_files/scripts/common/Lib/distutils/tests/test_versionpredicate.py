# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_versionpredicate.py
import distutils.versionpredicate, doctest
from test.test_support import run_unittest

def test_suite():
    return doctest.DocTestSuite(distutils.versionpredicate)


if __name__ == '__main__':
    run_unittest(test_suite())