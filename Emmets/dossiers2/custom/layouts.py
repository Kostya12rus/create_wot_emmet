# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/layouts.py
from dossiers2.common.DossierBlockBuilders import *
from account_layout import accountDossierLayout
from vehicle_layout import vehicleDossierLayout
from tankman_layout import tmanDossierLayout
from club_layout import rated7x7DossierLayout, clubDossierLayout
from dossiers2.custom.clan_layout import clanDossierLayout
VERSION_RECORD_FORMAT = 'H'
BLOCK_SIZE_RECORD_FORMAT = 'H'