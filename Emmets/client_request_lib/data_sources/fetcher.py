# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/client_request_lib/data_sources/fetcher.py
from soft_exception import SoftException

class FakeResponse(object):

    def __init__(self, r):
        self.responseCode = r.status_code
        self.body = r.raw.read()
        self._headers = r.headers

    def headers(self):
        return self._headers

    def __repr__(self):
        return ('[HTTP status: {}] {}').format(self.responseCode, self.body)


def fetchURL(url, callback, headers=None, timeout=30, method='GET', postData=''):
    import requests
    headers = headers or {}
    data = postData
    if isinstance(headers, (list, tuple)):
        res = {}
        for header in headers:
            a, b = header.split(':')
            res[a] = b

        headers = res
    if not isinstance(data, str) and data is not None:
        raise SoftException(('Unsupported parameter {}').format(data))
    methods = {'GET': requests.get, 
       'PUT': requests.put, 
       'POST': requests.post, 
       'PATCH': requests.patch, 
       'DELETE': requests.delete}
    if method in methods:
        response = methods[method](url, headers=headers, data=data, verify=False, stream=True)
    else:
        raise SoftException(('Unsupported method {}').format(method))
    callback(FakeResponse(response))
    return