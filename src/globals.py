import aiohttp
import weakref
from functools import partial
from werkzeug.local import LocalProxy


def _get_session(*args):
    return aiohttp.ClientSession()


_global_cache = weakref.WeakValueDictionary()

instance_map = {
    'session': _get_session,
}


def _get_object(name, *args):
    key = name + ''.join(args)
    if key in _global_cache:
        o = _global_cache[key]
    else:
        o = instance_map[name](*args)
        _global_cache[key] = o
    return o


session = LocalProxy(partial(_get_object, 'session'))
