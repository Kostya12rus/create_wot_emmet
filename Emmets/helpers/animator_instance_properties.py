# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/animator_instance_properties.py
from collections import namedtuple
AnimatorInstanceProperties = namedtuple('AnimatorInstanceProperties', ('delay', 'speed',
                                                                       'loopCount',
                                                                       'loop'))
AnimatorInstanceProperties.__new__.__defaults__ = (0.0, 1.0, -1, True)