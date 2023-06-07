# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/web/downloader.py


class IDownloader(object):

    @property
    def stopped(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def downloadLowPriority(self, url, callback):
        raise NotImplementedError

    def download(self, url, callback):
        raise NotImplementedError