# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/encodings/mac_arabic.py
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='mac-arabic', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({128: 196, 
   129: 160, 
   130: 199, 
   131: 201, 
   132: 209, 
   133: 214, 
   134: 220, 
   135: 225, 
   136: 224, 
   137: 226, 
   138: 228, 
   139: 1722, 
   140: 171, 
   141: 231, 
   142: 233, 
   143: 232, 
   144: 234, 
   145: 235, 
   146: 237, 
   147: 8230, 
   148: 238, 
   149: 239, 
   150: 241, 
   151: 243, 
   152: 187, 
   153: 244, 
   154: 246, 
   155: 247, 
   156: 250, 
   157: 249, 
   158: 251, 
   159: 252, 
   160: 32, 
   161: 33, 
   162: 34, 
   163: 35, 
   164: 36, 
   165: 1642, 
   166: 38, 
   167: 39, 
   168: 40, 
   169: 41, 
   170: 42, 
   171: 43, 
   172: 1548, 
   173: 45, 
   174: 46, 
   175: 47, 
   176: 1632, 
   177: 1633, 
   178: 1634, 
   179: 1635, 
   180: 1636, 
   181: 1637, 
   182: 1638, 
   183: 1639, 
   184: 1640, 
   185: 1641, 
   186: 58, 
   187: 1563, 
   188: 60, 
   189: 61, 
   190: 62, 
   191: 1567, 
   192: 10058, 
   193: 1569, 
   194: 1570, 
   195: 1571, 
   196: 1572, 
   197: 1573, 
   198: 1574, 
   199: 1575, 
   200: 1576, 
   201: 1577, 
   202: 1578, 
   203: 1579, 
   204: 1580, 
   205: 1581, 
   206: 1582, 
   207: 1583, 
   208: 1584, 
   209: 1585, 
   210: 1586, 
   211: 1587, 
   212: 1588, 
   213: 1589, 
   214: 1590, 
   215: 1591, 
   216: 1592, 
   217: 1593, 
   218: 1594, 
   219: 91, 
   220: 92, 
   221: 93, 
   222: 94, 
   223: 95, 
   224: 1600, 
   225: 1601, 
   226: 1602, 
   227: 1603, 
   228: 1604, 
   229: 1605, 
   230: 1606, 
   231: 1607, 
   232: 1608, 
   233: 1609, 
   234: 1610, 
   235: 1611, 
   236: 1612, 
   237: 1613, 
   238: 1614, 
   239: 1615, 
   240: 1616, 
   241: 1617, 
   242: 1618, 
   243: 1662, 
   244: 1657, 
   245: 1670, 
   246: 1749, 
   247: 1700, 
   248: 1711, 
   249: 1672, 
   250: 1681, 
   251: 123, 
   252: 124, 
   253: 125, 
   254: 1688, 
   255: 1746})
decoding_table = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7fÄ\xa0ÇÉÑÖÜáàâäں«çéèêëí…îïñó»ôö÷úùûü !"#$٪&\'()*+،-./٠١٢٣٤٥٦٧٨٩:؛<=>؟❊ءآأؤإئابةتثجحخدذرزسشصضطظعغ[\\]^_ـفقكلمنهوىيًٌٍَُِّْپٹچەڤگڈڑ{|}ژے'
encoding_map = {0: 0, 
   1: 1, 
   2: 2, 
   3: 3, 
   4: 4, 
   5: 5, 
   6: 6, 
   7: 7, 
   8: 8, 
   9: 9, 
   10: 10, 
   11: 11, 
   12: 12, 
   13: 13, 
   14: 14, 
   15: 15, 
   16: 16, 
   17: 17, 
   18: 18, 
   19: 19, 
   20: 20, 
   21: 21, 
   22: 22, 
   23: 23, 
   24: 24, 
   25: 25, 
   26: 26, 
   27: 27, 
   28: 28, 
   29: 29, 
   30: 30, 
   31: 31, 
   32: 32, 
   32: 160, 
   33: 33, 
   33: 161, 
   34: 34, 
   34: 162, 
   35: 35, 
   35: 163, 
   36: 36, 
   36: 164, 
   37: 37, 
   38: 38, 
   38: 166, 
   39: 39, 
   39: 167, 
   40: 40, 
   40: 168, 
   41: 41, 
   41: 169, 
   42: 42, 
   42: 170, 
   43: 43, 
   43: 171, 
   44: 44, 
   45: 45, 
   45: 173, 
   46: 46, 
   46: 174, 
   47: 47, 
   47: 175, 
   48: 48, 
   49: 49, 
   50: 50, 
   51: 51, 
   52: 52, 
   53: 53, 
   54: 54, 
   55: 55, 
   56: 56, 
   57: 57, 
   58: 58, 
   58: 186, 
   59: 59, 
   60: 60, 
   60: 188, 
   61: 61, 
   61: 189, 
   62: 62, 
   62: 190, 
   63: 63, 
   64: 64, 
   65: 65, 
   66: 66, 
   67: 67, 
   68: 68, 
   69: 69, 
   70: 70, 
   71: 71, 
   72: 72, 
   73: 73, 
   74: 74, 
   75: 75, 
   76: 76, 
   77: 77, 
   78: 78, 
   79: 79, 
   80: 80, 
   81: 81, 
   82: 82, 
   83: 83, 
   84: 84, 
   85: 85, 
   86: 86, 
   87: 87, 
   88: 88, 
   89: 89, 
   90: 90, 
   91: 91, 
   91: 219, 
   92: 92, 
   92: 220, 
   93: 93, 
   93: 221, 
   94: 94, 
   94: 222, 
   95: 95, 
   95: 223, 
   96: 96, 
   97: 97, 
   98: 98, 
   99: 99, 
   100: 100, 
   101: 101, 
   102: 102, 
   103: 103, 
   104: 104, 
   105: 105, 
   106: 106, 
   107: 107, 
   108: 108, 
   109: 109, 
   110: 110, 
   111: 111, 
   112: 112, 
   113: 113, 
   114: 114, 
   115: 115, 
   116: 116, 
   117: 117, 
   118: 118, 
   119: 119, 
   120: 120, 
   121: 121, 
   122: 122, 
   123: 123, 
   123: 251, 
   124: 124, 
   124: 252, 
   125: 125, 
   125: 253, 
   126: 126, 
   127: 127, 
   160: 129, 
   171: 140, 
   187: 152, 
   196: 128, 
   199: 130, 
   201: 131, 
   209: 132, 
   214: 133, 
   220: 134, 
   224: 136, 
   225: 135, 
   226: 137, 
   228: 138, 
   231: 141, 
   232: 143, 
   233: 142, 
   234: 144, 
   235: 145, 
   237: 146, 
   238: 148, 
   239: 149, 
   241: 150, 
   243: 151, 
   244: 153, 
   246: 154, 
   247: 155, 
   249: 157, 
   250: 156, 
   251: 158, 
   252: 159, 
   1548: 172, 
   1563: 187, 
   1567: 191, 
   1569: 193, 
   1570: 194, 
   1571: 195, 
   1572: 196, 
   1573: 197, 
   1574: 198, 
   1575: 199, 
   1576: 200, 
   1577: 201, 
   1578: 202, 
   1579: 203, 
   1580: 204, 
   1581: 205, 
   1582: 206, 
   1583: 207, 
   1584: 208, 
   1585: 209, 
   1586: 210, 
   1587: 211, 
   1588: 212, 
   1589: 213, 
   1590: 214, 
   1591: 215, 
   1592: 216, 
   1593: 217, 
   1594: 218, 
   1600: 224, 
   1601: 225, 
   1602: 226, 
   1603: 227, 
   1604: 228, 
   1605: 229, 
   1606: 230, 
   1607: 231, 
   1608: 232, 
   1609: 233, 
   1610: 234, 
   1611: 235, 
   1612: 236, 
   1613: 237, 
   1614: 238, 
   1615: 239, 
   1616: 240, 
   1617: 241, 
   1618: 242, 
   1632: 176, 
   1633: 177, 
   1634: 178, 
   1635: 179, 
   1636: 180, 
   1637: 181, 
   1638: 182, 
   1639: 183, 
   1640: 184, 
   1641: 185, 
   1642: 165, 
   1657: 244, 
   1662: 243, 
   1670: 245, 
   1672: 249, 
   1681: 250, 
   1688: 254, 
   1700: 247, 
   1711: 248, 
   1722: 139, 
   1746: 255, 
   1749: 246, 
   8230: 147, 
   10058: 192}