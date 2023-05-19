# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/new.py
from warnings import warnpy3k
warnpy3k("The 'new' module has been removed in Python 3.0; use the 'types' module instead.", stacklevel=2)
del warnpy3k
from types import ClassType as classobj
from types import FunctionType as function
from types import InstanceType as instance
from types import MethodType as instancemethod
from types import ModuleType as module
from types import CodeType as code