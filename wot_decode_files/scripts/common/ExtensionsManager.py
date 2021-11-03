# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/ExtensionsManager.py
import BigWorld, os, ResMgr
from collections import namedtuple
Extension = namedtuple('Extension', ('path', 'name', 'isEnabled'))

class ExtensionsManager(object):

    def __init__(self):
        self.__extensions = {}
        for root, dirs, files in os.walk('../wot_ext'):
            if 'extension.xml' in files:
                extension = self.__readExtension(root)
                self.__extensions[extension.name] = extension

    def __readExtension(self, root):
        section = ResMgr.openSection(root + '/extension.xml')
        return Extension(root + '/', section.readString('FeatureName'), section.readBool('IsEnabled'))

    @property
    def extensions(self):
        return self.__extensions.values()


g_extensionsManager = ExtensionsManager()