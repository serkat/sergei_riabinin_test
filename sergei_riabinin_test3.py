import datetime
import random


class OrmucoCache:
    """
    Generally, caching algorithm is:
        def memoize(func):
            our_cache = {}
            def memoized_func(*args):
                if args in our_cache:
                    return our_cache[args]
                result = func(*args)
                our_cache[args] = result
                return result
            return memoized_func

    """
    def __init__(self):
        self.cache = {}  # dictionary as a cache - key, value
        self.max_cache_size = 5

    def __contains__(self, key):
        """
        Check if key is in the cache
        :param key: cache key
        :return: True or False
        """
        return key in self.cache

    def update(self, key, value):
        """
        Update cache dictionary and remove the oldest cache. Also remove if the max cache value is reached or exceeded
        :param key: cache key
        :param value: cache value
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_old()
        self.cache[key] = {'access_date': datetime.datetime.now(), 'value': value}

    def remove_old(self):
        """
        remove item with the oldest date
        """
        old_item = None
        for key in self.cache:
            if old_item is None:
                old_item = key
            elif self.cache[key]['access_date'] < self.cache[old_item]['access_date']:
                old_item = key
        del self.cache[old_item]

    @property
    def cache_size(self):
        """
        Get the size of cache
        :return: len
        """
        return len(self.cache)


if __name__ == '__main__':
    # Test the cache
    keys = ['some', 'test', 'for', 'cache', 'entries',
            'with', 'random', 'data', 'here']
    s = 'abcdefghijklmnopqrstuvwxyz'
    cache = OrmucoCache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(s) for i in range(36)])
            cache.update(key, value)
        print("#%s iterations, #%s cached entries" % (i + 1, cache.cache_size))
