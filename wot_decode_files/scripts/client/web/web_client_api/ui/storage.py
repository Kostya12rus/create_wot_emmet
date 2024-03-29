# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/storage.py
from gui.Scaleform.daapi.view.lobby.storage import getSectionsList
from gui.shared import event_dispatcher as shared_events
from web.web_client_api import w2c, W2CSchema, Field, WebCommandException

def _validateSection(value, _):
    if value in (section['id'] for section in getSectionsList()):
        return True
    raise WebCommandException(value)


class _OpenStorageSchema(W2CSchema):
    section_id = Field(required=False, type=basestring, validator=_validateSection)


class StorageWebApiMixin(object):

    @w2c(_OpenStorageSchema, 'storage')
    def openStorage(self, cmd):
        sectionId = cmd.section_id
        if sectionId is not None:
            shared_events.showStorage(sectionId)
        else:
            shared_events.showStorage()
        return