# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/doc_loaders/__init__.py
import ResMgr
from messenger.doc_loaders import colors_schemes, html_templates, settings_set
from messenger.doc_loaders import user_prefs
from messenger.doc_loaders._xml_helpers import XMLCtx, XMLError
from messenger.m_constants import MESSENGER_XML_FILE_PATH
_LOADERS = (
 (
  'defUserPreferences', False, user_prefs.loadDefault),
 (
  'colorsSchemes', True, colors_schemes.load),
 (
  'settingsSet', True, settings_set.load),
 (
  'htmlTemplatesSimple', True, html_templates.loadForOthers),
 (
  'htmlTemplates', True, html_templates.loadForMessage))

def load(messengerSettings):
    section = ResMgr.openSection(MESSENGER_XML_FILE_PATH)
    xmlCtx = XMLCtx(MESSENGER_XML_FILE_PATH)
    if section is None:
        raise XMLError(xmlCtx, 'Messenger settings file is not found')
    tags = section.keys()
    for tag, isRequired, loader in _LOADERS:
        if tag in tags:
            subSec = section[tag]
            loader(xmlCtx.next(subSec), subSec, messengerSettings)
        elif isRequired:
            raise XMLError(xmlCtx, ('Tag "{0:>s}" not found').format(tag))

    ResMgr.purge(MESSENGER_XML_FILE_PATH, True)
    return