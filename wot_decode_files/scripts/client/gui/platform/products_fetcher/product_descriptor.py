# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/product_descriptor.py
from helpers.events_handler import EventsHandler

class ProductDescriptor(EventsHandler):

    def __init__(self, params):
        self._params = params
        self._isFull = False
        self._subscribe()

    @property
    def productCode(self):
        return self._getFromParams('product_code', '')

    @property
    def productID(self):
        return self._getFromParams('product_id', '')

    @property
    def productUrl(self):
        return self._getFromParams('product_url', '')

    @property
    def metadata(self):
        return self._getFromParams('metadata', {}).get('wot', {})

    @property
    def description(self):
        return self._getFromMetadata('description')

    @property
    def largeImageURL(self):
        return self._getImageURL('large')

    @property
    def smallImageURL(self):
        return self._getImageURL('small')

    @property
    def mediumImageURL(self):
        return self._getImageURL('medium')

    @property
    def shortDescription(self):
        return self._getFromMetadata('short_description')

    @property
    def name(self):
        return self._getFromMetadata('name')

    @property
    def claimURL(self):
        return self.metadata.get('claimURL', {}).get('data', '')

    @property
    def isDescriptorFull(self):
        return self._isFull

    def destroy(self):
        self._unsubscribe()

    def extendData(self, data):
        self._isFull = True
        self._params.update(data)

    def _getImageURL(self, size):
        return self.metadata.get('image_' + size, {}).get('data', {}).get('url', {}).get('value', '')

    def _getFromParams(self, name, default=None):
        return self._params.get(name, default)

    def _getFromMetadata(self, valueName):
        return self.metadata.get(valueName, {}).get('data', {}).get('value', '')