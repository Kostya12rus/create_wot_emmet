# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/EmptyEntity.py
import BigWorld

class EmptyEntity(BigWorld.Entity):

    def __init__(self):
        super(EmptyEntity, self).__init__()
        self.filter = BigWorld.AvatarFilter()

    def onLeaveWorld(self):
        pass