# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/ext/filters/__init__.py
from gui import GUI_SETTINGS
from messenger import g_settings
from messenger.ext.filters import chain, collection
from messenger.storage import storage_getter
__all__ = ('MessageFiltersChain', )

class MessageFiltersChain(chain.FiltersChain):

    def __init__(self):
        inFilters = [
         {'name': 'htmlEscape', 
            'filter': collection.HtmlEscapeFilter(), 
            'order': 0, 
            'lock': True}]
        outFilters = [
         {'name': 'normalizeLobbyMessage', 
            'filter': collection.NormalizeMessageFilter(), 
            'order': 0, 
            'lock': False}]
        super(MessageFiltersChain, self).__init__(inFilters, outFilters)

    @storage_getter('playerCtx')
    def playerCtx(self):
        return

    def init(self):
        g_settings.onUserPreferencesUpdated += self.__ms_onUserPreferencesUpdated
        self.playerCtx.onAccountAttrsChanged += self.__pc_onAccountAttrsChanged
        self.__ms_onUserPreferencesUpdated()

    def fini(self):
        g_settings.onUserPreferencesUpdated -= self.__ms_onUserPreferencesUpdated
        self.playerCtx.onAccountAttrsChanged -= self.__pc_onAccountAttrsChanged

    def __ms_onUserPreferencesUpdated(self):
        if GUI_SETTINGS.postBattleExchange.enabled:
            self.addFilter('postBattleFilter', collection.PostBattleLinksFilter())
        if g_settings.userPrefs.enableOlFilter:
            if not self.hasFilter('enableOlFilter'):
                self.addFilter('olFilter', collection.getObsceneLanguageFilter(), removed=[
                 'coloringOlFilter'])
        else:
            ctx = self.playerCtx
            isAdmin = ctx.isChatAdmin() or ctx.isGameAdmin()
            if isAdmin and not self.hasFilter('coloringOlFilter'):
                self.addFilter('coloringOlFilter', collection.ColoringObsceneLanguageFilter(), removed=[
                 'olFilter'])
            else:
                self.removeFilter('olFilter')
        if g_settings.userPrefs.enableSpamFilter:
            self.addFilter('domainFilter', collection.DomainNameFilter())
            self.addFilter('spamFilter', collection.SpamFilter())
            self.addFilter('floodFilter', collection.FloodFilter())
        else:
            self.removeFilter('domainFilter')
            self.removeFilter('spamFilter')
            self.removeFilter('floodFilter')

    def __pc_onAccountAttrsChanged(self):
        ctx = self.playerCtx
        if ctx.isChatAdmin() or ctx.isGameAdmin():
            if not g_settings.userPrefs.enableOlFilter and not self.hasFilter('coloringOlFilter'):
                self.addFilter('coloringOlFilter', collection.ColoringObsceneLanguageFilter(), removed=[
                 'olFilter'])
        else:
            self.removeFilter('coloringOlFilter')