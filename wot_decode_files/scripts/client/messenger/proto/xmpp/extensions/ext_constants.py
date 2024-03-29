# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/xmpp/extensions/ext_constants.py


class XML_NAME_SPACE(object):
    BLOCKING_CMD = 'urn:xmpp:blocking'
    CHAT_STATES = 'http://jabber.org/protocol/chatstates'
    DELAY = 'urn:xmpp:delay'
    STANZA_ERROR = 'urn:ietf:params:xml:ns:xmpp-stanzas'
    RESULT_SET_MANAGEMENT = 'http://jabber.org/protocol/rsm'
    DISCO_ITEMS = 'http://jabber.org/protocol/disco#items'
    DISCO_INFO = 'http://jabber.org/protocol/disco#info'
    MUC_OWNER = 'http://jabber.org/protocol/muc#owner'
    DATA_FORMS = 'jabber:x:data'
    WG_EXTENSION = 'http://wargaming.net/xmpp#v2'
    WG_EXTENSION_EXTRA = 'http://wargaming.net/xmpp#extra-attributes'
    WG_CLIENT = 'http://wargaming.net/xmpp#client'
    WG_SPA_RESOLVER = 'http://wargaming.net/xmpp#spa-resolver'
    WG_STORAGE = 'http://wargaming.net/xmpp#storage'
    WG_PRIVATE_HISTORY = 'http://wargaming.net/xmpp#private-message-history'
    WG_MESSAGE_ID = 'http://wargaming.net/xmpp#message-id'
    WG_MUC_ROOMS = 'http://wargaming.net/xmpp#filter-muc-rooms-disco'
    WG_DISCO_ITEMS = 'http://wargaming.net/xmpp#disco#items:wgexts'


class XML_TAG_NAME(object):
    BLOCK_LIST = 'blocklist'
    BLOCK_ITEM = 'block'
    UNBLOCK_ITEM = 'unblock'
    MESSAGE = 'message'
    DELAY = 'delay'
    QUERY = 'query'
    LIST = 'list'
    ITEM = 'item'
    ERROR = 'error'
    SET = 'set'
    FILTER = 'filter'
    CRITERION = 'criterion'
    X = 'x'
    FIELD = 'field'
    VALUE = 'value'
    IDENTITY = 'identity'
    FEATURE = 'feature'
    CREATED_BY = 'created-by'
    WG_EXTENSION = 'wgexts'
    WG_CLIENT = 'wgexts-client'
    WG_PRIVATE_HISTORY = 'private-history'
    WG_MESSAGE_ID = 'message-id'
    WG_NICKNAME_PREFIX_SEARCH = 'nickname-prefix-search'
    WG_MUC_PRIVILEGES = 'muc-privileges'
    WG_EXTENSION_EXTRA = 'extra'