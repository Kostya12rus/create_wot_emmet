# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/GraphicsPresets.py
import BigWorld, ResMgr
graphicsPresetsResource = 'system/data/graphics_settings_presets.xml'

class GraphicsPresets:

    def __init__(self):
        sect = ResMgr.openSection(graphicsPresetsResource)
        self.entries = {}
        self.entryNames = []
        self.selectedOption = -1
        for group in sect.values():
            if group.asString != '':
                entry = {}
                for setting in group.values():
                    if setting.name == 'entry':
                        entry[setting.readString('label')] = setting.readInt('activeOption')

                self.entries[group.asString] = entry
                self.entryNames.append(group.asString)

        self.setSelectedOption()

    def setSelectedOption(self):
        self.selectedOption = -1
        currentOptionMap = {}
        for currentOption in BigWorld.graphicsSettings():
            currentOptionMap[currentOption[0]] = currentOption[1]

        for i in range(0, len(self.entryNames)):
            foundOption = True
            for setting in self.entries[self.entryNames[i]].items():
                if currentOptionMap.get(setting[0]) != setting[1]:
                    foundOption = False
                    break

            if foundOption == True:
                self.selectedOption = i
                break

    def selectGraphicsOptions(self, option):
        currentOption = self.entries[self.entryNames[option]]
        for setting in currentOption.items():
            try:
                BigWorld.setGraphicsSetting(setting[0], setting[1])
            except:
                print 'selectGraphicsOptions: unable to set option ', setting[0]

        self.selectedOption = option