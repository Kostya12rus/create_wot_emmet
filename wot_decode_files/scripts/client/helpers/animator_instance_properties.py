# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/animator_instance_properties.py
from collections import namedtuple
AnimatorInstanceProperties = namedtuple('AnimatorInstanceProperties', ('delay', 'speed',
                                                                       'loopCount',
                                                                       'loop'))
AnimatorInstanceProperties.__new__.__defaults__ = (0.0, 1.0, -1, True)