# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/errors.py
__revision__ = '$Id$'

class DistutilsError(Exception):
    pass


class DistutilsModuleError(DistutilsError):
    pass


class DistutilsClassError(DistutilsError):
    pass


class DistutilsGetoptError(DistutilsError):
    pass


class DistutilsArgError(DistutilsError):
    pass


class DistutilsFileError(DistutilsError):
    pass


class DistutilsOptionError(DistutilsError):
    pass


class DistutilsSetupError(DistutilsError):
    pass


class DistutilsPlatformError(DistutilsError):
    pass


class DistutilsExecError(DistutilsError):
    pass


class DistutilsInternalError(DistutilsError):
    pass


class DistutilsTemplateError(DistutilsError):
    pass


class DistutilsByteCompileError(DistutilsError):
    pass


class CCompilerError(Exception):
    pass


class PreprocessError(CCompilerError):
    pass


class CompileError(CCompilerError):
    pass


class LibError(CCompilerError):
    pass


class LinkError(CCompilerError):
    pass


class UnknownFileError(CCompilerError):
    pass