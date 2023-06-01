# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/loggers.py
import logging

def getLogger(loggerName):
    return logging.getLogger(('GameLoading:{}').format(loggerName))


def getSequencesViewHistoryLogger():
    return getLogger('SequencesViewHistory')


def getCdnConfigLogger():
    return getLogger('CdnConfig')


def getCdnCacheLogger():
    return getLogger('CdnCache')


def getResourcesLogger():
    return getLogger('Resources')


def getStatesLogger():
    return getLogger('States')


def getStateMachineLogger():
    return getLogger('StateMachine')


def getLoaderSettingsLogger():
    return getLogger('LoaderSettings')


def getLoaderLogger():
    return getLogger('Loader')