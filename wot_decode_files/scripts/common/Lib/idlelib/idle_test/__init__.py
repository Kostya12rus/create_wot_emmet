# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/idle_test/__init__.py
from os.path import dirname

def load_tests(loader, standard_tests, pattern):
    this_dir = dirname(__file__)
    top_dir = dirname(dirname(this_dir))
    package_tests = loader.discover(start_dir=this_dir, pattern='test*.py', top_level_dir=top_dir)
    standard_tests.addTests(package_tests)
    return standard_tests