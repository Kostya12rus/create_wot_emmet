# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/web/cache/web_downloader.py
from functools import partial
from helpers import threads
from gui.shared.RemoteDataDownloader import _HttpOpenUrlJob
from helpers.web.downloader import IDownloader
from shared_utils import nextTick

class WebDownloader(IDownloader):

    def __init__(self, workersLimit, queueLimit=threads.INFINITE_QUEUE_SIZE):
        self.__worker = threads.ThreadPool(workersLimit, queueLimit)
        self.__worker.start()

    def close(self):
        if self.__worker:
            self.__worker.stop()
            self.__worker = None
        return

    def downloadLowPriority(self, url, callback):
        self.__worker.putLowPriorityJob(_HttpOpenUrlJob(url, None, partial(self.__onDownload, url, callback)))
        return

    def download(self, url, callback):
        self.__worker.putJob(_HttpOpenUrlJob(url, None, partial(self.__onDownload, url, callback)))
        return

    def __onDownload(self, url, callback, data, lastModified, expires):
        nextTick(partial(callback, url, data))()