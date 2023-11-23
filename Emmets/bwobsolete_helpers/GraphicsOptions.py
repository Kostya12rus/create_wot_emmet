# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bwobsolete_helpers/GraphicsOptions.py
import ResMgr, sys, BigWorld
tex_detail_levels = ResMgr.openSection('system/data/texture_detail_levels.xml')

def normalMapsCompressed():
    ns = tex_detail_levels.values()[0]
    if ns.readString('format') == 'A8R8G8B8':
        return False
    return True


def compressNormalMaps(state):
    ns = tex_detail_levels.values()[0]
    ns.writeString('format', 'A8R8G8B8')
    BigWorld.reloadTextures()


def optIncludeOptionEnabled(value):
    filename = '../../bigworld/res/shaders/std_effects/optinclude.fxh'
    try:
        f = open(filename, 'r')
    except IOError:
        print 'Failed to open %s' % (filename,)
        return

    output = []
    lines = f.readlines()
    changed = False
    found = False
    for line in lines:
        if value in line:
            found = True
            if '//' in line:
                return False
            return True

    return False


def enableOptincludeOption(value, enable):
    filename = '../../bigworld/res/shaders/std_effects/optinclude.fxh'
    try:
        f = open(filename, 'r')
    except IOError:
        print 'Failed to open %s' % (filename,)
        return

    output = []
    lines = f.readlines()
    changed = False
    found = False
    for line in lines:
        if value in line:
            found = True
            if '//' in line:
                if enable:
                    line = '#define ' + value + ' 1\n'
                    changed = True
            elif not enable:
                line = '//#define ' + value + ' 1\n'
                changed = True
        output.append(line)

    if enable and not found:
        output.append('#define ' + value + ' 1')
        changed = True
    f.close()
    if changed and len(output) > 0:
        f = open(filename, 'w+')
        if f == None:
            print 'Could not open %s for writing' % (filename,)
            return
        f.writelines(output)
        f.close()
    return