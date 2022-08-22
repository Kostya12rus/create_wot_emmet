# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/Util.py
import BigWorld

def entitiesFromChunk(sectionName):
    import ResMgr
    sects = ResMgr.openSection(sectionName)
    if sects != None:
        for sect in sects.values():
            if sect.name == 'entity':
                type = sect.readString('type')
                pos = sect.readVector3('transform/row3')
                dict = {}
                for props in sect['properties'].values():
                    try:
                        dict[str(props.name)] = eval(props.asString)
                    except:
                        dict[str(props.name)] = props.asString

                BigWorld.createEntity(type, BigWorld.player().spaceID, 0, pos, (0,
                                                                                0,
                                                                                0), dict)

    return