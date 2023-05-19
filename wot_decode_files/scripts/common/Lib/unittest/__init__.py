# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/unittest/__init__.py
__all__ = [
 'TestResult', 'TestCase', 'TestSuite', 
 'TextTestRunner', 'TestLoader', 
 'FunctionTestCase', 'main', 
 'defaultTestLoader', 'SkipTest', 'skip', 'skipIf', 
 'skipUnless', 
 'expectedFailure', 'TextTestResult', 'installHandler', 
 'registerResult', 
 'removeResult', 'removeHandler']
__all__.extend(['getTestCaseNames', 'makeSuite', 'findTestCases'])
__unittest = True
from .result import TestResult
from .case import TestCase, FunctionTestCase, SkipTest, skip, skipIf, skipUnless, expectedFailure
from .suite import BaseTestSuite, TestSuite
from .loader import TestLoader, defaultTestLoader, makeSuite, getTestCaseNames, findTestCases
from .main import TestProgram, main
from .runner import TextTestRunner, TextTestResult
from .signals import installHandler, registerResult, removeResult, removeHandler
_TextTestResult = TextTestResult