# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/bootcamp/states/__init__.py


class STATE(object):
    INITIAL = 0
    BATTLE_PREPARING = 1
    IN_BATTLE = 2
    RESULT_SCREEN = 3
    IN_GARAGE = 4
    OUTRO_VIDEO = 5
    FINISHING = 6