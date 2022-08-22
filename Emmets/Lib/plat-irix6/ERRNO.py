# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/plat-irix6/ERRNO.py
from warnings import warnpy3k
warnpy3k('the ERRNO module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
__KBASE = 1000
__IRIXBASE = 1000
__FTNBASE = 4000
__FTNLAST = 5999
EPERM = 1
ENOENT = 2
ESRCH = 3
EINTR = 4
EIO = 5
ENXIO = 6
E2BIG = 7
ENOEXEC = 8
EBADF = 9
ECHILD = 10
EAGAIN = 11
ENOMEM = 12
EACCES = 13
EFAULT = 14
ENOTBLK = 15
EBUSY = 16
EEXIST = 17
EXDEV = 18
ENODEV = 19
ENOTDIR = 20
EISDIR = 21
EINVAL = 22
ENFILE = 23
EMFILE = 24
ENOTTY = 25
ETXTBSY = 26
EFBIG = 27
ENOSPC = 28
ESPIPE = 29
EROFS = 30
EMLINK = 31
EPIPE = 32
EDOM = 33
ERANGE = 34
ENOMSG = 35
EIDRM = 36
ECHRNG = 37
EL2NSYNC = 38
EL3HLT = 39
EL3RST = 40
ELNRNG = 41
EUNATCH = 42
ENOCSI = 43
EL2HLT = 44
EDEADLK = 45
ENOLCK = 46
ECKPT = 47
EBADE = 50
EBADR = 51
EXFULL = 52
ENOANO = 53
EBADRQC = 54
EBADSLT = 55
EDEADLOCK = 56
EBFONT = 57
ENOSTR = 60
ENODATA = 61
ETIME = 62
ENOSR = 63
ENONET = 64
ENOPKG = 65
EREMOTE = 66
ENOLINK = 67
EADV = 68
ESRMNT = 69
ECOMM = 70
EPROTO = 71
EMULTIHOP = 74
EBADMSG = 77
ENAMETOOLONG = 78
EOVERFLOW = 79
ENOTUNIQ = 80
EBADFD = 81
EREMCHG = 82
ELIBACC = 83
ELIBBAD = 84
ELIBSCN = 85
ELIBMAX = 86
ELIBEXEC = 87
EILSEQ = 88
ENOSYS = 89
ELOOP = 90
ERESTART = 91
ESTRPIPE = 92
ENOTEMPTY = 93
EUSERS = 94
ENOTSOCK = 95
EDESTADDRREQ = 96
EMSGSIZE = 97
EPROTOTYPE = 98
ENOPROTOOPT = 99
EPROTONOSUPPORT = 120
ESOCKTNOSUPPORT = 121
EOPNOTSUPP = 122
EPFNOSUPPORT = 123
EAFNOSUPPORT = 124
EADDRINUSE = 125
EADDRNOTAVAIL = 126
ENETDOWN = 127
ENETUNREACH = 128
ENETRESET = 129
ECONNABORTED = 130
ECONNRESET = 131
ENOBUFS = 132
EISCONN = 133
ENOTCONN = 134
ESHUTDOWN = 143
ETOOMANYREFS = 144
ETIMEDOUT = 145
ECONNREFUSED = 146
EHOSTDOWN = 147
EHOSTUNREACH = 148
LASTERRNO = ENOTCONN
EWOULDBLOCK = __KBASE + 101
EWOULDBLOCK = EAGAIN
EALREADY = 149
EINPROGRESS = 150
ESTALE = 151
EIORESID = 500
EUCLEAN = 135
ENOTNAM = 137
ENAVAIL = 138
EISNAM = 139
EREMOTEIO = 140
EINIT = 141
EREMDEV = 142
ECANCELED = 158
ENOLIMFILE = 1001
EPROCLIM = 1002
EDISJOINT = 1003
ENOLOGIN = 1004
ELOGINLIM = 1005
EGROUPLOOP = 1006
ENOATTACH = 1007
ENOTSUP = 1008
ENOATTR = 1009
EFSCORRUPTED = 1010
EDIRCORRUPTED = 1010
EWRONGFS = 1011
EDQUOT = 1133
ENFSREMOTE = 1135
ECONTROLLER = 1300
ENOTCONTROLLER = 1301
EENQUEUED = 1302
ENOTENQUEUED = 1303
EJOINED = 1304
ENOTJOINED = 1305
ENOPROC = 1306
EMUSTRUN = 1307
ENOTSTOPPED = 1308
ECLOCKCPU = 1309
EINVALSTATE = 1310
ENOEXIST = 1311
EENDOFMINOR = 1312
EBUFSIZE = 1313
EEMPTY = 1314
ENOINTRGROUP = 1315
EINVALMODE = 1316
ECANTEXTENT = 1317
EINVALTIME = 1318
EDESTROYED = 1319
EBDHDL = 1400
EDELAY = 1401
ENOBWD = 1402
EBADRSPEC = 1403
EBADTSPEC = 1404
EBADFILT = 1405
EMIGRATED = 1500
EMIGRATING = 1501
ECELLDOWN = 1502
EMEMRETRY = 1600