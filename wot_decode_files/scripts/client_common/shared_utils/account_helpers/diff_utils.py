# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client_common/shared_utils/account_helpers/diff_utils.py
_KEY_DELIMITER = '.'

def synchronizeDicts(diff, cache, parentKey='', changeList=None, defaultCacheType=dict):
    updates, replaces, deletes = (0, 0, 0)
    if parentKey != '':
        parentKey = parentKey + _KEY_DELIMITER
    keys_r, keys_d, keys_u = [], [], []
    for k in diff.iterkeys():
        if changeList is not None and isinstance(k, basestring):
            changeList[parentKey + k] = diff[k]
        if isinstance(k, tuple):
            if k[1] == '_r':
                keys_r.append(k)
                replaces += 1
                continue
            elif k[1] == '_d':
                keys_d.append(k)
                deletes += 1
                if changeList is not None:
                    changeList[k[0] + k[1]] = diff[k]
                continue
        keys_u.append(k)
        updates += 1

    for key_r in keys_r:
        cache[key_r[0]] = diff[key_r]

    for key_d in keys_d:
        value = cache.get(key_d[0], None)
        if value:
            value.difference_update(diff[key_d])

    for key_u in keys_u:
        value = diff[key_u]
        if value is None:
            cache.pop(key_u, None)
        elif isinstance(value, dict):
            newParentKey = parentKey + str(key_u) if changeList is not None else ''
            result = synchronizeDicts(value, cache.setdefault(key_u, defaultCacheType()), newParentKey, changeList, defaultCacheType)
            updates, replaces, deletes = [ i + j for i, j in zip((updates, replaces, deletes), result) ]
        elif isinstance(value, set):
            cache.setdefault(key_u, set()).update(value)
        else:
            cache[key_u] = value

    return (
     updates, replaces, deletes)