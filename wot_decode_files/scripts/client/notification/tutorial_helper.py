# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/notification/tutorial_helper.py
try:
    from tutorial import GlobalStorage as TutorialGlobalStorage
    from tutorial.control.context import GLOBAL_VAR as TUTORIAL_GLOBAL_VAR
except ImportError:

    class TutorialGlobalStorage(object):

        def __init__(self, *args):
            pass

        def __get__(self, instance, owner=None):
            if instance is None:
                return self
            else:
                return 0


    class TUTORIAL_GLOBAL_VAR(object):
        LAST_HISTORY_ID = ''
        SERVICE_MESSAGES_IDS = ''