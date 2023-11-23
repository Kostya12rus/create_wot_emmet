# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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