# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/http/url_formatters.py
import typing, urllib, urlparse

class URL_PARTS_IDS(object):
    SCHEME = 0
    NETLOC = 1
    PATH = 2
    PARAMS = 3
    QUERY = 4
    FRAGMENT = 5


def addParamsToUrlQuery(url, params, keepBlankValues=False):
    urlParts = list(urlparse.urlparse(url))
    query = urlparse.parse_qs(urlParts[URL_PARTS_IDS.QUERY], keep_blank_values=keepBlankValues)
    query.update(params)
    urlParts[URL_PARTS_IDS.QUERY] = urllib.urlencode(query, True)
    return urlparse.urlunparse(urlParts)


def separateQuery(url):
    urlParts = list(urlparse.urlparse(url))
    mainUrlParts = urlParts[:URL_PARTS_IDS.QUERY] + ['', '']
    queryParts = [''] * 4 + urlParts[URL_PARTS_IDS.QUERY:]
    return (urlparse.urlunparse(mainUrlParts), urlparse.urlunparse(queryParts))