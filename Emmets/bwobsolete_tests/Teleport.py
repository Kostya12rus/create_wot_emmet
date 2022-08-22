# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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