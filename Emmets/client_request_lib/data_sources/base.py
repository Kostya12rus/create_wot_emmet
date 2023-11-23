# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/client_request_lib/data_sources/base.py
from abc import ABCMeta, abstractmethod
__all__ = ('BaseDataAccessor', )

class BaseDataAccessor(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def login(self, callback, account_id, token, jwt):
        pass

    @abstractmethod
    def logout(self, callback):
        pass

    @abstractmethod
    def get_clans_ratings(self, callback, clan_ids, fields=None):
        pass

    @abstractmethod
    def get_accounts_names(self, callback, account_ids):
        pass

    @abstractmethod
    def get_clan_invites(self, callback, clan_id, fields=None, statuses=None, offset=0, limit=18):
        pass

    @abstractmethod
    def get_account_invites(self, callback, account_id, fields=None, statuses=None, offset=0, limit=18):
        pass

    @abstractmethod
    def get_account_applications_count_since(self, callback, account_id, since=None):
        pass

    @abstractmethod
    def get_clan_invites_count_since(self, callback, clan_id, since=None):
        pass

    @abstractmethod
    def get_clan_applications(self, callback, clan_id, fields=None, statuses=None, offset=0, limit=18):
        pass

    @abstractmethod
    def search_clans(self, callback, search, get_total_count=False, fields=None, offset=0, limit=18):
        pass

    @abstractmethod
    def get_clans_info(self, callback, clan_ids, fields=None):
        pass

    @abstractmethod
    def get_clan_members(self, callback, clan_id, fields=None):
        pass

    @abstractmethod
    def get_clan_favorite_attributes(self, callback, clan_id, fields=None):
        pass

    @abstractmethod
    def get_accounts_clans(self, callback, account_ids, fields=None):
        pass

    @abstractmethod
    def get_accounts_info(self, callback, account_ids, fields=None):
        pass

    @abstractmethod
    def get_clan_provinces(self, callback, clan_id, fields=None):
        pass

    @abstractmethod
    def get_clan_globalmap_stats(self, callback, clan_id, fields=None):
        pass

    @abstractmethod
    def get_fronts_info(self, callback, front_names=None, fields=None):
        pass

    @abstractmethod
    def get_stronghold_info(self, callback, clan_id=None, fields=None):
        pass

    @abstractmethod
    def get_strongholds_statistics(self, callback, clan_id, fields=None):
        pass

    @abstractmethod
    def get_strongholds_state(self, callback, clan_id, fields=None):
        pass