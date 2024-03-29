# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/ContactInfo.py
import Settings

class ContactInfo(object):
    KEY_USER = 'user'
    KEY_HOST = 'host'
    KEY_EMAIL = 'email'
    KEY_PASSWORD = 'password'
    KEY_REMEMBER = 'remember'

    def __init__(self):
        self.host = None
        self.user = None
        self.email = None
        self.password = None
        self.rememberPassword = False
        self.__checkLoginDataSection()
        self.readLocalLoginData()
        return

    def readLocalLoginData(self):
        ds = self.getLoginDataSection()
        self.host = ds.readString(self.KEY_HOST)
        self.user = ds.readString(self.KEY_USER)
        self.email = ds.readString(self.KEY_EMAIL)
        self.password = ds.readString(self.KEY_PASSWORD)
        self.rememberPassword = bool(ds.readString(self.KEY_REMEMBER))

    def writeLocalLoginData(self):
        ds = self.getLoginDataSection()
        ds.writeString(self.KEY_HOST, self.host)
        ds.writeString(self.KEY_USER, self.user)
        ds.writeString(self.KEY_EMAIL, self.email)
        ds.writeString(self.KEY_PASSWORD, self.password)
        ds.writeString(self.KEY_REMEMBER, str(self.rememberPassword))

    def getLoginDataSection(self):
        return Settings.g_instance.userPrefs[Settings.KEY_LOGIN_INFO]

    def __checkLoginDataSection(self):
        up = Settings.g_instance.userPrefs
        if not up.has_key(Settings.KEY_LOGIN_INFO):
            up.write(Settings.KEY_LOGIN_INFO, '')