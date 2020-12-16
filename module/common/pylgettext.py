#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gettext import *

_searchdirs = None

origfind = find

def setpaths(pathlist):
    global _searchdirs
    _searchdirs = pathlist if isinstance(pathlist, list) else list(pathlist)


def addpath(path):
    global _searchdirs
    if _searchdirs is None:
        _searchdirs = list(path)
    else:
        if path not in _searchdirs:
            _searchdirs.append(path)


def delpath(path):
    global _searchdirs
    if _searchdirs is not None and path in _searchdirs:
        _searchdirs.remove(path)


def clearpath():
    global _searchdirs
    if _searchdirs is not None:
        _searchdirs = None


def find(domain, localedir=None, languages=None, all=False):
    if _searchdirs is None:
        return origfind(domain, localedir, languages, all)
    searches = [localedir] + _searchdirs
    results = []
    for dir in searches:
        res = origfind(domain, dir, languages, all)
        if all is False:
            results.append(res)
        else:
            results.extend(res)
    if all is not False:
        return results

    results = filter(lambda x: x is not None, results)
    if len(results) == 0:
        return None
    else:
        return results[0]

#Is there a smarter/cleaner pythonic way for this?
translation.func_globals['find'] = find
