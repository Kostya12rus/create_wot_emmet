# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/promo_screens/parsers.py


class PromoDataParser(object):
    _ALL_FIELDS_MAP = {'unread': 'count', 
       'sent_at': 'timestamp', 
       'data': 'lastPromo'}
    _DATA_FIELDS_MAP = {'id': 'promoID', 
       'promo_name': 'description', 
       'image': 'image', 
       'promoscreen_url': 'url', 
       'version_name': 'version', 
       'video': 'video', 
       'expiration_time': 'finishTime', 
       'type': 'promoType', 
       'slug': 'slug'}
    _DATA_FIELD_NAME = 'data'
    _INT_FIELDS = ('id', 'unread', 'sent_at', 'expiration_time')

    @classmethod
    def parse(cls, data):
        return cls.__abstractParse(data, cls.__extractFromArray)

    @classmethod
    def parseXML(cls, data):
        return cls.__abstractParse(data, cls.__extractFromXML)

    @classmethod
    def __abstractParse(cls, data, extractor):
        result = {}
        promoData = {}
        for source, target in cls._ALL_FIELDS_MAP.iteritems():
            if source == cls._DATA_FIELD_NAME:
                promoData = result[target] = {}
            else:
                result[target] = extractor(data, source)

        promoDataSource = data[cls._DATA_FIELD_NAME]
        for source, target in cls._DATA_FIELDS_MAP.iteritems():
            promoData[target] = extractor(promoDataSource, source)

        return result

    @classmethod
    def __extractFromXML(cls, data, key):
        if key in cls._INT_FIELDS:
            return data.readInt(key)
        return data.readString(key)

    @staticmethod
    def __extractFromArray(data, key):
        return data.get(key)