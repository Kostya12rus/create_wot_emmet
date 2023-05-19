# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_tests/Teleport.py
import BigWorld, Math, math, random
from functools import partial

def teleportNext(timer, destinationList):
    dest = destinationList[0]
    BigWorld.player().tryToTeleport(dest[0], dest[1])
    if len(destinationList) > 1:
        BigWorld.callback(timer, partial(teleportNext, timer, destinationList[1:]))
    else:
        print 'teleport test finished'


def testTeleport():
    d = []
    d.append(['spaces/highlands', 'demo2'])
    d.append(['spaces/highlands', 'demo3'])
    d.append(['spaces/highlands', 'demo4'])
    d.append(['spaces/arctic', 'demo1'])
    d.append(['spaces/arctic', 'demo2'])
    d.append(['spaces/arctic', 'demo3'])
    d.append(['spaces/arctic', 'demo4'])
    d.append(['spaces/highlands', 'demo1'])
    BigWorld.callback(0.1, partial(teleportNext, 20, d))