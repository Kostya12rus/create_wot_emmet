# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/doc_loaders/GuiDirReader.py
import ResMgr

class GuiDirReader(object):
    SCALEFORM_STARTUP_VIDEO_PATH = 'gui/flash/videos/startup'
    SCALEFORM_STARTUP_VIDEO_MASK = 'videos/startup/%s'
    VIDEO_EXTENSION = 'usm'

    @staticmethod
    def getAvailableIntroVideoFiles():
        ds = ResMgr.openSection(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH)
        movieFiles = []
        if ds is None:
            return movieFiles
        else:
            for filename in ds.keys():
                try:
                    _, extension = filename.split('.')
                except ValueError:
                    continue

                _, extension = filename.split('.')
                if extension == GuiDirReader.VIDEO_EXTENSION:
                    movieFiles.append(GuiDirReader.SCALEFORM_STARTUP_VIDEO_MASK % filename)

            ResMgr.purge(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH, True)
            return movieFiles