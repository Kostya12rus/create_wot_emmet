# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/findertools.py
from warnings import warnpy3k
warnpy3k('In 3.x, the findertools module is removed.', stacklevel=2)
import Finder
from Carbon import AppleEvents
import aetools, MacOS, sys, Carbon.File, Carbon.Folder, aetypes
from types import *
__version__ = '1.1'
Error = 'findertools.Error'
_finder_talker = None

def _getfinder():
    global _finder_talker
    if not _finder_talker:
        _finder_talker = Finder.Finder()
    _finder_talker.send_flags = _finder_talker.send_flags | AppleEvents.kAECanInteract | AppleEvents.kAECanSwitchLayer
    return _finder_talker


def launch(file):
    finder = _getfinder()
    fss = Carbon.File.FSSpec(file)
    return finder.open(fss)


def Print(file):
    finder = _getfinder()
    fss = Carbon.File.FSSpec(file)
    return finder._print(fss)


def copy(src, dstdir):
    finder = _getfinder()
    if type(src) == type([]):
        src_fss = []
        for s in src:
            src_fss.append(Carbon.File.FSSpec(s))

    else:
        src_fss = Carbon.File.FSSpec(src)
    dst_fss = Carbon.File.FSSpec(dstdir)
    return finder.duplicate(src_fss, to=dst_fss)


def move(src, dstdir):
    finder = _getfinder()
    if type(src) == type([]):
        src_fss = []
        for s in src:
            src_fss.append(Carbon.File.FSSpec(s))

    else:
        src_fss = Carbon.File.FSSpec(src)
    dst_fss = Carbon.File.FSSpec(dstdir)
    return finder.move(src_fss, to=dst_fss)


def sleep():
    finder = _getfinder()
    finder.sleep()


def shutdown():
    finder = _getfinder()
    finder.shut_down()


def restart():
    finder = _getfinder()
    finder.restart()


def reveal(file):
    finder = _getfinder()
    fsr = Carbon.File.FSRef(file)
    file_alias = fsr.FSNewAliasMinimal()
    return finder.reveal(file_alias)


def select(file):
    finder = _getfinder()
    fsr = Carbon.File.FSRef(file)
    file_alias = fsr.FSNewAliasMinimal()
    return finder.select(file_alias)


def update(file):
    finder = _getfinder()
    fsr = Carbon.File.FSRef(file)
    file_alias = fsr.FSNewAliasMinimal()
    return finder.update(file_alias)


def comment(object, comment=None):
    object = Carbon.File.FSRef(object)
    object_alias = object.FSNewAliasMinimal()
    if comment is None:
        return _getcomment(object_alias)
    else:
        return _setcomment(object_alias, comment)
        return


def _setcomment(object_alias, comment):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cobj'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('comt'), fr=aeobj_00)
    args['----'] = aeobj_01
    args['data'] = comment
    _reply, args, attrs = finder.send('core', 'setd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def _getcomment(object_alias):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cobj'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('comt'), fr=aeobj_00)
    args['----'] = aeobj_01
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def processes():
    finder = _getfinder()
    args = {}
    attrs = {}
    processnames = []
    processnumbers = []
    creators = []
    partitions = []
    used = []
    args['----'] = aetypes.ObjectSpecifier(want=aetypes.Type('prcs'), form='indx', seld=aetypes.Unknown('abso', 'all '), fr=None)
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    p = []
    if '----' in args:
        p = args['----']
        for proc in p:
            if hasattr(proc, 'seld'):
                processnames.append(proc.seld)
            elif hasattr(proc, 'type'):
                if proc.type == 'psn ':
                    processnumbers.append(proc.data)

    args = {}
    attrs = {}
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('prcs'), form='indx', seld=aetypes.Unknown('abso', 'all '), fr=None)
    args['----'] = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('fcrt'), fr=aeobj_0)
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(_arg)
    if '----' in args:
        p = args['----']
        creators = p[:]
    result = []
    if len(processnames) > len(processnumbers):
        data = processnames
    else:
        data = processnumbers
    for i in range(len(creators)):
        result.append((data[i], creators[i]))

    return result


class _process:
    pass


def isactiveprocess(processname):
    all = processes()
    ok = 0
    for n, c in all:
        if n == processname:
            return 1

    return 0


def processinfo(processname):
    p = _process()
    if processname == 'Finder':
        p.partition = None
        p.used = None
    else:
        p.partition = _processproperty(processname, 'appt')
        p.used = _processproperty(processname, 'pusd')
    p.visible = _processproperty(processname, 'pvis')
    p.frontmost = _processproperty(processname, 'pisf')
    p.file = _processproperty(processname, 'file')
    p.filetype = _processproperty(processname, 'asty')
    p.creatortype = _processproperty(processname, 'fcrt')
    p.accepthighlevel = _processproperty(processname, 'revt')
    p.hasscripting = _processproperty(processname, 'hscr')
    return p


def _processproperty(processname, property):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('prcs'), form='name', seld=processname, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type(property), fr=aeobj_00)
    args['----'] = aeobj_01
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def openwindow(object):
    finder = _getfinder()
    object = Carbon.File.FSRef(object)
    object_alias = object.FSNewAliasMinimal()
    args = {}
    attrs = {}
    _code = 'aevt'
    _subcode = 'odoc'
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=object_alias, fr=None)
    args['----'] = aeobj_0
    _reply, args, attrs = finder.send(_code, _subcode, args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    return


def closewindow(object):
    finder = _getfinder()
    object = Carbon.File.FSRef(object)
    object_alias = object.FSNewAliasMinimal()
    args = {}
    attrs = {}
    _code = 'core'
    _subcode = 'clos'
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=object_alias, fr=None)
    args['----'] = aeobj_0
    _reply, args, attrs = finder.send(_code, _subcode, args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    return


def location(object, pos=None):
    object = Carbon.File.FSRef(object)
    object_alias = object.FSNewAliasMinimal()
    if not pos:
        return _getlocation(object_alias)
    return _setlocation(object_alias, pos)


def _setlocation(object_alias, (x, y)):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('posn'), fr=aeobj_00)
    args['----'] = aeobj_01
    args['data'] = [x, y]
    _reply, args, attrs = finder.send('core', 'setd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    return (
     x, y)


def _getlocation(object_alias):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('posn'), fr=aeobj_00)
    args['----'] = aeobj_01
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        pos = args['----']
        return (
         pos.h, pos.v)
    else:
        return


def label(object, index=None):
    object = Carbon.File.FSRef(object)
    object_alias = object.FSNewAliasMinimal()
    if index is None:
        return _getlabel(object_alias)
    else:
        if index < 0 or index > 7:
            index = 0
        return _setlabel(object_alias, index)


def _getlabel(object_alias):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cobj'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('labi'), fr=aeobj_00)
    args['----'] = aeobj_01
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def _setlabel(object_alias, index):
    finder = _getfinder()
    args = {}
    attrs = {}
    _code = 'core'
    _subcode = 'setd'
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='alis', seld=object_alias, fr=None)
    aeobj_1 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('labi'), fr=aeobj_0)
    args['----'] = aeobj_1
    args['data'] = index
    _reply, args, attrs = finder.send(_code, _subcode, args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    return index


def windowview(folder, view=None):
    fsr = Carbon.File.FSRef(folder)
    folder_alias = fsr.FSNewAliasMinimal()
    if view is None:
        return _getwindowview(folder_alias)
    else:
        return _setwindowview(folder_alias, view)


def _setwindowview(folder_alias, view=0):
    attrs = {}
    args = {}
    if view == 1:
        _v = aetypes.Type('pnam')
    elif view == 2:
        _v = aetypes.Type('lgbu')
    else:
        _v = aetypes.Type('iimg')
    finder = _getfinder()
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=folder_alias, fr=None)
    aeobj_1 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('cwnd'), fr=aeobj_0)
    aeobj_2 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('pvew'), fr=aeobj_1)
    aeobj_3 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=_v, fr=None)
    _code = 'core'
    _subcode = 'setd'
    args['----'] = aeobj_2
    args['data'] = aeobj_3
    _reply, args, attrs = finder.send(_code, _subcode, args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def _getwindowview(folder_alias):
    attrs = {}
    args = {}
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=folder_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('cwnd'), fr=aeobj_00)
    aeobj_02 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('pvew'), fr=aeobj_01)
    args['----'] = aeobj_02
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    views = {'iimg': 0, 'pnam': 1, 'lgbu': 2}
    if '----' in args:
        return views[args['----'].enum]
    else:
        return


def windowsize(folder, size=None):
    fsr = Carbon.File.FSRef(folder)
    folder_alias = fsr.FSNewAliasMinimal()
    openwindow(fsr)
    if not size:
        return _getwindowsize(folder_alias)
    return _setwindowsize(folder_alias, size)


def _setwindowsize(folder_alias, (w, h)):
    finder = _getfinder()
    args = {}
    attrs = {}
    _code = 'core'
    _subcode = 'setd'
    aevar00 = [w, h]
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=folder_alias, fr=None)
    aeobj_1 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('cwnd'), fr=aeobj_0)
    aeobj_2 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('ptsz'), fr=aeobj_1)
    args['----'] = aeobj_2
    args['data'] = aevar00
    _reply, args, attrs = finder.send(_code, _subcode, args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    return (
     w, h)


def _getwindowsize(folder_alias):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=folder_alias, fr=None)
    aeobj_1 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('cwnd'), fr=aeobj_0)
    aeobj_2 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('posn'), fr=aeobj_1)
    args['----'] = aeobj_2
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def windowposition(folder, pos=None):
    fsr = Carbon.File.FSRef(folder)
    folder_alias = fsr.FSNewAliasMinimal()
    openwindow(fsr)
    if not pos:
        return _getwindowposition(folder_alias)
    if type(pos) == InstanceType:
        pos = (pos.h, pos.v)
    return _setwindowposition(folder_alias, pos)


def _setwindowposition(folder_alias, (x, y)):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=folder_alias, fr=None)
    aeobj_1 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('cwnd'), fr=aeobj_0)
    aeobj_2 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('posn'), fr=aeobj_1)
    args['----'] = aeobj_2
    args['data'] = [x, y]
    _reply, args, attrs = finder.send('core', 'setd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def _getwindowposition(folder_alias):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_0 = aetypes.ObjectSpecifier(want=aetypes.Type('cfol'), form='alis', seld=folder_alias, fr=None)
    aeobj_1 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('cwnd'), fr=aeobj_0)
    aeobj_2 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('ptsz'), fr=aeobj_1)
    args['----'] = aeobj_2
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def icon(object, icondata=None):
    fsr = Carbon.File.FSRef(object)
    object_alias = fsr.FSNewAliasMinimal()
    if icondata is None:
        return _geticon(object_alias)
    else:
        return _seticon(object_alias, icondata)


def _geticon(object_alias):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cobj'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('iimg'), fr=aeobj_00)
    args['----'] = aeobj_01
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def _seticon(object_alias, icondata):
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('cobj'), form='alis', seld=object_alias, fr=None)
    aeobj_01 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('iimg'), fr=aeobj_00)
    args['----'] = aeobj_01
    args['data'] = icondata
    _reply, args, attrs = finder.send('core', 'setd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----'].data
    else:
        return


def mountvolume(volume, server=None, username=None, password=None):
    finder = _getfinder()
    args = {}
    attrs = {}
    if password:
        args['PASS'] = password
    if username:
        args['USER'] = username
    if server:
        args['SRVR'] = server
    args['----'] = volume
    _reply, args, attrs = finder.send('aevt', 'mvol', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']


def unmountvolume(volume):
    putaway(volume)


def putaway(object):
    finder = _getfinder()
    args = {}
    attrs = {}
    args['----'] = aetypes.ObjectSpecifier(want=aetypes.Type('cdis'), form='name', seld=object, fr=None)
    _reply, args, attrs = talker.send('fndr', 'ptwy', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def volumelevel(level):
    finder = _getfinder()
    args = {}
    attrs = {}
    if level < 0:
        level = 0
    else:
        if level > 7:
            level = 7
        args['----'] = level
        _reply, args, attrs = finder.send('aevt', 'stvl', args, attrs)
        if 'errn' in args:
            raise Error, aetools.decodeerror(args)
        if '----' in args:
            return args['----']


def OSversion():
    finder = _getfinder()
    args = {}
    attrs = {}
    aeobj_00 = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('ver2'), fr=None)
    args['----'] = aeobj_00
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        return args['----']
    else:
        return


def filesharing():
    status = -1
    finder = _getfinder()
    args = {}
    attrs = {}
    args['----'] = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('fshr'), fr=None)
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        if args['----'] == 0:
            status = -1
        else:
            status = 1
    args = {}
    attrs = {}
    args['----'] = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('fsup'), fr=None)
    _reply, args, attrs = finder.send('core', 'getd', args, attrs)
    if 'errn' in args:
        raise Error, aetools.decodeerror(args)
    if '----' in args:
        if args['----'] == 1:
            status = 0
    return status


def movetotrash(path):
    fss = Carbon.File.FSSpec(path)
    trashfolder = Carbon.Folder.FSFindFolder(fss.as_tuple()[0], 'trsh', 0)
    move(path, trashfolder)


def emptytrash():
    finder = _getfinder()
    args = {}
    attrs = {}
    args['----'] = aetypes.ObjectSpecifier(want=aetypes.Type('prop'), form='prop', seld=aetypes.Type('trsh'), fr=None)
    _reply, args, attrs = finder.send('fndr', 'empt', args, attrs)
    if 'errn' in args:
        raise aetools.Error, aetools.decodeerror(args)
    return


def _test():
    import EasyDialogs
    print 'Original findertools functionality test...'
    print 'Testing launch...'
    pathname = EasyDialogs.AskFileForOpen('File to launch:')
    if pathname:
        result = launch(pathname)
        if result:
            print 'Result: ', result
        print 'Press return-',
        sys.stdin.readline()
    print 'Testing print...'
    pathname = EasyDialogs.AskFileForOpen('File to print:')
    if pathname:
        result = Print(pathname)
        if result:
            print 'Result: ', result
        print 'Press return-',
        sys.stdin.readline()
    print 'Testing copy...'
    pathname = EasyDialogs.AskFileForOpen('File to copy:')
    if pathname:
        destdir = EasyDialogs.AskFolder('Destination:')
        if destdir:
            result = copy(pathname, destdir)
            if result:
                print 'Result:', result
            print 'Press return-',
            sys.stdin.readline()
    print 'Testing move...'
    pathname = EasyDialogs.AskFileForOpen('File to move:')
    if pathname:
        destdir = EasyDialogs.AskFolder('Destination:')
        if destdir:
            result = move(pathname, destdir)
            if result:
                print 'Result:', result
            print 'Press return-',
            sys.stdin.readline()
    print 'Testing sleep...'
    if EasyDialogs.AskYesNoCancel('Sleep?') > 0:
        result = sleep()
        if result:
            print 'Result:', result
        print 'Press return-',
        sys.stdin.readline()
    print 'Testing shutdown...'
    if EasyDialogs.AskYesNoCancel('Shut down?') > 0:
        result = shutdown()
        if result:
            print 'Result:', result
        print 'Press return-',
        sys.stdin.readline()
    print 'Testing restart...'
    if EasyDialogs.AskYesNoCancel('Restart?') > 0:
        result = restart()
        if result:
            print 'Result:', result
        print 'Press return-',
        sys.stdin.readline()


def _test2():
    print '\nmorefindertools version %s\nTests coming up...' % __version__
    import os, random
    print '\tfilesharing on?', filesharing()
    print '\tOS version', OSversion()
    print '\tSystem beep volume'
    for i in range(0, 7):
        volumelevel(i)
        MacOS.SysBeep()

    open('@findertoolstest', 'w')
    f = '@findertoolstest'
    reveal(f)
    select(f)
    base, file = os.path.split(f)
    closewindow(base)
    openwindow(base)
    windowview(base, 1)
    label(f, 2)
    print '\tlabel', label(f)
    print 'Random locations for an icon'
    windowview(base, 0)
    windowsize(base, (600, 600))
    for i in range(50):
        location(f, (random.randint(10, 590), random.randint(10, 590)))

    windowsize(base, (200, 400))
    windowview(base, 1)
    orgpos = windowposition(base)
    print 'Animated window location'
    for i in range(10):
        pos = (
         100 + i * 10, 100 + i * 10)
        windowposition(base, pos)
        print '\twindow position', pos

    windowposition(base, orgpos)
    print 'Put a comment in file', f, ':'
    print '\t', comment(f)
    s = 'This is a comment no one reads!'
    comment(f, s)


def _test3():
    print 'MacOS9 or better specific functions'
    pr = processes()
    print 'Return a list of current active processes:'
    for p in pr:
        print '\t', p

    print 'Attributes of the first process in the list:'
    pinfo = processinfo(pr[0][0])
    print '\t', pr[0][0]
    print '\t\tmemory partition', pinfo.partition
    print '\t\tmemory used', pinfo.used
    print '\t\tis visible', pinfo.visible
    print '\t\tis frontmost', pinfo.frontmost
    print '\t\thas scripting', pinfo.hasscripting
    print '\t\taccepts high level events', pinfo.accepthighlevel


if __name__ == '__main__':
    _test()
    _test2()
    _test3()