# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/VersionUpdater.py
import sys
from debug_utils import LOG_DEBUG

class VersionUpdaterBase(object):

    def __init__(self, template, latestVersion, moduleWithUpdaters=None):
        self._startVersion = None
        self._updaters = None
        self._template = template
        self._latestVersion = latestVersion
        self._module = moduleWithUpdaters
        if moduleWithUpdaters is None:
            self._module = sys.modules[self.__module__]
        return

    latestVersion = property((lambda self: self._latestVersion))

    def __buildUpdaters(self):
        self._updaters = []
        for fromVer in xrange(self._latestVersion):
            args = (fromVer,) if self._template.count('%d') == 1 else (fromVer, fromVer + 1)
            funcName = self._template % args
            func = getattr(self._module, funcName, None)
            if func is not None:
                self._updaters.append(func)
                if self._startVersion is None:
                    self._startVersion = fromVer

        LOG_DEBUG('__buildUpdaters', self.__class__, self._startVersion, self._latestVersion)
        return

    def __getUpdaters(self, startVersion):
        if startVersion == self._latestVersion:
            return []
        else:
            if self._updaters is None:
                self.__buildUpdaters()
            return enumerate(self._updaters[startVersion - self._startVersion:], start=startVersion)

    def _updateToLatestVersion(self, versionOrGetter, checkerForCallback, logID, *args):
        isCallable = callable(versionOrGetter)
        currentVersion = versionOrGetter(*args) if isCallable else versionOrGetter
        for fromVer, updater in self.__getUpdaters(currentVersion):
            LOG_DEBUG('_updateToLatestVersion', logID, fromVer)
            result = updater(*args)
            checkerForCallback(result, updater, *args)
            if isCallable:
                resultVer = versionOrGetter(*args)
            else:
                resultVer, args = result[0], result[1:]
            if resultVer == self._latestVersion:
                break

        return args