# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/wrappers/function_helpers.py
import functools

def replaceNoneKwargsModel(func):

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if 'model' not in kwargs:
            actual = None
        else:
            actual = kwargs['model']
        if actual is None:
            with self.getViewModel().transaction() as (model):
                kwargs['model'] = model
                return func(self, *args, **kwargs)
        else:
            return func(self, *args, **kwargs)
        return

    return wrapper