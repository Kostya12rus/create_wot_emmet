# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/validate_shells.py
import ResMgr

def gatherChunks(spaceDir):
    if spaceDir[-1] != '/':
        spaceDir = spaceDir + '/'
    result = []
    entries = ResMgr.openSection(spaceDir)
    if entries:
        for entry in entries.keys():
            if entry[0] == '.':
                continue
            if ResMgr.isDir(spaceDir + entry):
                children = gatherChunks(spaceDir + entry)
                result.extend(children)
            else:
                entry = entry.lower()
                if len(entry) == 15 and entry[-6:] == '.chunk':
                    result.append(spaceDir + entry)

    return result


def validateShells(spaceDir):
    if spaceDir[-1] != '/':
        spaceDir = spaceDir + '/'
    chunks = gatherChunks(spaceDir)
    shells = [ x for x in chunks if x[-7] == 'i' ]
    outsides = [ x for x in chunks if x[-7] == 'o' ]
    for chunk in outsides:
        section = ResMgr.openSection(chunk)
        overlappers = section.readStrings('overlapper')
        for overlapper in overlappers:
            shell = spaceDir + overlapper + '.chunk'
            if shell in shells:
                shells.remove(shell)

    print shells