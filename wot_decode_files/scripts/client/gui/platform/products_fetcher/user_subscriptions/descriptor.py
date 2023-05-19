# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/user_subscriptions/descriptor.py


class UserSubscriptionDescriptor(object):

    def __init__(self, data):
        self._params = data

    @property
    def productCode(self):
        return self._params.get('product_code')

    @property
    def status(self):
        return self._params.get('status')