# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/common/DossierBuilder.py
import struct
from typing import Callable, Tuple
from DossierDescr import DossierDescr
from dossiers2.common.DossierBlockBuilders import TYPE_BLOCK_BUILDER
from dossiers2.custom.updaters import DossierVersionUpdaterBase

class DossierBuilder(object):

    def __init__(self, blockBuilders, versionFormat, blockSizeFormat, version, updater, initializer):
        self.__blockBuilders = blockBuilders
        self.__versionFormat = versionFormat
        self.__headerFormat = '<' + versionFormat + blockSizeFormat * len(blockBuilders)
        self.__latestVersion = version
        self.__updater = updater
        self.__initializer = initializer
        self.__emptyCompDescr = struct.pack(self.__headerFormat, version, *([0] * len(blockBuilders)))

    def build(self, compDescr=''):
        if compDescr == '':
            dossier = DossierDescr(self.__emptyCompDescr, self.__blockBuilders, self.__headerFormat)
            self.__initializer(dossier)
        else:
            version = struct.unpack_from(self.__versionFormat, compDescr)[0]
            compDescr = self.__updater.updateVersion(version, compDescr)
            dossier = DossierDescr(compDescr, self.__blockBuilders, self.__headerFormat)
        return dossier