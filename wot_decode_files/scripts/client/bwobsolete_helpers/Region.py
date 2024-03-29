# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/Region.py
import BigWorld, FantasyDemo

class Region:

    def __init__(self):
        self.currentSpace = ''
        self.currentRegion = None
        self.currentDesc = ''
        self.listeners = []
        FantasyDemo.addChangeEnvironmentsListener(self.onChangeEnvironments)
        return

    def fini(self):
        FantasyDemo.delChangeEnvironmentsListener(self.onChangeEnvironments)

    def addListener(self, l):
        self.listeners.append(l)
        l.onEnterRegion(self.describeCurrent())

    def delListener(self, l):
        try:
            self.listeners.remove(l)
        except ValueError:
            pass

    def describeCurrent(self):
        if self.currentRegion != None:
            return self.currentRegion
        else:
            return self.currentSpace
            return

    def onChangeEnvironments(self, inside):
        player = BigWorld.player()
        if player != None:
            spaceID = player.spaceID
            try:
                self.currentSpace = self.fancify(FantasyDemo.rds.spaceNameMap[spaceID])
            except KeyError:
                self.currentSpace = ''

            self.checkForChanges()
        return

    def fancify(self, name):
        name = name.split('spaces/')[-1]
        name = name.replace('_', ' ')
        name = name.title()
        return name

    def onEnterRegion(self, description):
        if self.currentRegion != description:
            self.currentRegion = description
            self.checkForChanges()

    def onLeaveRegion(self, description):
        if self.currentRegion == description:
            self.currentRegion = None
            self.checkForChanges()
        return

    def checkForChanges(self):
        desc = self.describeCurrent()
        if self.currentDesc != desc:
            self.currentDesc = desc
            for l in self.listeners:
                l.onEnterRegion(desc)