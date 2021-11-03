# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/maps_training/maps_training_client_settings.py
import Settings
_INCOMPLETE_FILTER_KEY = 'incompleteFilter'

class MapsTrainingClientSettings(object):

    def __init__(self):
        self.__userPrefs = None
        self.incompleteFilter = False
        self.titleFilter = ''
        return

    def load(self):
        self.__userPrefs = Settings.g_instance.userPrefs
        if self.__userPrefs is None or not self.__userPrefs.has_key(Settings.KEY_MAPS_TRAINING_PREFERENCES):
            return
        ds = self.__userPrefs[Settings.KEY_MAPS_TRAINING_PREFERENCES]
        self.incompleteFilter = ds.readBool(_INCOMPLETE_FILTER_KEY, False)
        return

    def save(self):
        if not self.__userPrefs.has_key(Settings.KEY_MAPS_TRAINING_PREFERENCES):
            self.__userPrefs.write(Settings.KEY_MAPS_TRAINING_PREFERENCES, '')
        ds = self.__userPrefs[Settings.KEY_MAPS_TRAINING_PREFERENCES]
        ds.writeBool(_INCOMPLETE_FILTER_KEY, self.incompleteFilter)

    def resetSessionFilters(self):
        self.titleFilter = ''