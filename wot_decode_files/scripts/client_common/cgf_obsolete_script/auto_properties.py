# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/cgf_obsolete_script/auto_properties.py


class AutoProperty(object):

    def __init__(self, fieldName=None):
        self.fieldName = fieldName

    def __get__(self, instance, owner=None):
        if instance is not None:
            return getattr(instance, self.fieldName, None)
        else:
            return self

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)


class TypedProperty(AutoProperty):

    def __init__(self, allowedType, fieldName=None):
        AutoProperty.__init__(self, fieldName)
        self.allowedType = allowedType

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)


class LinkDescriptor(AutoProperty):

    def __init__(self, fieldName=None):
        AutoProperty.__init__(self, fieldName)

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)

    def __call__(self, *args, **kwargs):
        return


class AutoPropertyInitMetaclass(type):

    def __new__(mcs, name, bases, attributes):
        for attributeName, attribute in attributes.iteritems():
            if isinstance(attribute, AutoProperty) and attribute.fieldName is None:
                attribute.fieldName = '_%s__%s' % (name, attributeName)

        return super(AutoPropertyInitMetaclass, mcs).__new__(mcs, name, bases, attributes)