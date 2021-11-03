# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-mac/appletrunner.py
from warnings import warnpy3k
warnpy3k('In 3.x, the appletrunner module is removed.', stacklevel=2)
import os, sys
for name in ['__rawmain__.py', '__rawmain__.pyc', '__main__.py', '__main__.pyc']:
    realmain = os.path.join(os.path.dirname(os.path.dirname(sys.argv[0])), 'Resources', name)
    if os.path.exists(realmain):
        break
else:
    sys.stderr.write('%s: cannot find applet main program\n' % sys.argv[0])
    sys.exit(1)

sys.argv.insert(1, realmain)
os.execve(sys.executable, sys.argv, os.environ)