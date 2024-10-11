# Extracted from https://stackoverflow.com/questions/16475384/rename-a-dictionary-key
import timeit
import random

# Efficiency tests
from collections import MutableMapping

class OrderedDictRaymond(dict, MutableMapping):
    def __init__(self, *args, **kwds):
        if len(args) > 1:
            raise TypeError('expected at 1 argument, got %d', len(args))
        if not hasattr(self, '_keys'):
            self._keys = []
        self.update(*args, **kwds)

    def rename(self,key,new_key):
        ind = self._keys.index(key)  #get the index of old key, O(N) operation
        self._keys[ind] = new_key    #replace old key with new key in self._keys
        self[new_key] = self[key]    #add the new key, this is added at the end of self._keys
        self._keys.pop(-1)           #pop the last item in self._keys
        dict.__delitem__(self, key)

    def clear(self):
        del self._keys[:]
        dict.clear(self)

    def __setitem__(self, key, value):
        if key not in self:
            self._keys.append(key)
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._keys.remove(key)

    def __iter__(self):
        return iter(self._keys)

    def __reversed__(self):
        return reversed(self._keys)

    def popitem(self):
        if not self:
            raise KeyError
        key = self._keys.pop()
        value = dict.pop(self, key)
        return key, value

    def __reduce__(self):
        items = [[k, self[k]] for k in self]
        inst_dict = vars(self).copy()
        inst_dict.pop('_keys', None)
        return (self.__class__, (items,), inst_dict)

    setdefault = MutableMapping.setdefault
    update = MutableMapping.update
    pop = MutableMapping.pop
    keys = MutableMapping.keys
    values = MutableMapping.values
    items = MutableMapping.items

    def __repr__(self):
        pairs = ', '.join(map('%r: %r'.__mod__, self.items()))
        return '%s({%s})' % (self.__class__.__name__, pairs)

    def copy(self):
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        d = cls()
        for key in iterable:
            d[key] = value
        return d

class obj_container:
    def __init__(self, obj) -> None:
        self.obj = obj

def change_key_splice(container, k_old, k_new):
    od = container.obj
    container.obj = OrderedDict((k_new if k == k_old else k, v) for k, v in od.items())

def change_key_raymond(container, k_old, k_new):
    od = container.obj
    od.rename(k_old, k_new)

def change_key_odx(container, k_old, k_new):
    odx = container.obj
    odx.change_key(k_old, k_new)

NUM_ITEMS = 20000
od_splice = OrderedDict([(x, x) for x in range(NUM_ITEMS)])
od_raymond = OrderedDictRaymond(od_splice.items())
odx = OrderedDictX(od_splice.items())
od_splice, od_raymond, odx = [obj_container(d) for d in [od_splice, od_raymond, odx]]
assert odx.obj == od_splice.obj
assert odx.obj == od_raymond.obj
# Pick randomly half of the keys to change
keys_to_change = random.sample(range(NUM_ITEMS), NUM_ITEMS//2)
print(f'OrderedDictX: {timeit.timeit(lambda: [change_key_odx(odx, k, k+NUM_ITEMS) for k in keys_to_change], number=1)}')
print(f'OrderedDictRaymond: {timeit.timeit(lambda: [change_key_raymond(od_raymond, k, k+NUM_ITEMS) for k in keys_to_change], number=1)}')
print(f'Splice: {timeit.timeit(lambda: [change_key_splice(od_splice, k, k+NUM_ITEMS) for k in keys_to_change], number=1)}')
assert odx.obj == od_splice.obj
assert odx.obj == od_raymond.obj

OrderedDictX: 0.06587849999999995
OrderedDictRaymond: 1.1131364
Splice: 1165.2614647

NUM_ITEMS = 100000
OrderedDictX: 0.3636919999999999
OrderedDictRaymond: 36.3963971

from collections import OrderedDict


class OrderedDictX(OrderedDict):
    def __init__(self, *args, **kwargs):
        # Mappings from new->old (ext2int), old->new (int2ext).
        # Only the keys that are changed (internal key doesn't match what the user sees) are contained.
        self._keys_ext2int = OrderedDict()
        self._keys_int2ext = OrderedDict()
        self.update(*args, **kwargs)

    def change_key(self, k_old, k_new):
        # Validate that the old key is part of the dict
        if not self.__contains__(k_old):
            raise Exception(f'Cannot rename key {k_old} to {k_new}: {k_old} not existing in dict')

        # Return if no changing is actually to be done
        if len(OrderedDict.fromkeys([k_old, k_new])) == 1:
            return

        # Validate that the new key would not conflict with another one
        if self.__contains__(k_new):
            raise Exception(f'Cannot rename key {k_old} to {k_new}: {k_new} already in dict')

        # Change the key using internal dicts mechanism
        if k_old in self._keys_ext2int:
            # Revert change temporarily
            k_old_int = self._keys_ext2int[k_old]
            del self._keys_ext2int[k_old]
            k_old = k_old_int
            # Check if new key matches the internal key
            if len(OrderedDict.fromkeys([k_old, k_new])) == 1:
                del self._keys_int2ext[k_old]
                return

        # Finalize key change
        self._keys_ext2int[k_new] = k_old
        self._keys_int2ext[k_old] = k_new

    def __contains__(self, k) -> bool:
        if k in self._keys_ext2int:
            return True
        if not super().__contains__(k):
            return False
        return k not in self._keys_int2ext

    def __getitem__(self, k):
        if not self.__contains__(k):
            # Intentionally raise KeyError in ext2int
            return self._keys_ext2int[k]
        return super().__getitem__(self._keys_ext2int.get(k, k))

    def __setitem__(self, k, v):
        if k in self._keys_ext2int:
            return super().__setitem__(self._keys_ext2int[k], v)
        # If the key exists in the internal state but was renamed to a k_ext,
        # employ this trick: make it such that it appears as if k_ext has also been renamed to k
        if k in self._keys_int2ext:
            k_ext = self._keys_int2ext[k]
            self._keys_ext2int[k] = k_ext
            k = k_ext
        return super().__setitem__(k, v)

    def __delitem__(self, k):
        if not self.__contains__(k):
            # Intentionally raise KeyError in ext2int
            del self._keys_ext2int[k]
        if k in self._keys_ext2int:
            k_int = self._keys_ext2int[k]
            del self._keys_ext2int[k]
            del self._keys_int2ext[k_int]
            k = k_int
        return super().__delitem__(k)

    def __iter__(self):
        yield from self.keys()

    def __reversed__(self):
        for k in reversed(super().keys()):
            yield self._keys_int2ext.get(k, k)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, dict):
            return False
        if len(self) != len(other):
            return False
        for (k, v), (k_other, v_other) in zip(self.items(), other.items()):
            if k != k_other or v != v_other:
                return False
        return True

    def update(self, *args, **kwargs):
        for k, v in OrderedDict(*args, **kwargs).items():
            self.__setitem__(k, v)

    def popitem(self, last=True) -> tuple:
        if not last:
            k = next(iter(self.keys()))
        else:
            k = next(iter(reversed(self.keys())))
        v = self.__getitem__(k)
        self.__delitem__(k)
        return k, v

    class OrderedDictXKeysView:
        def __init__(self, odx: 'OrderedDictX', orig_keys):
            self._odx = odx
            self._orig_keys = orig_keys

        def __iter__(self):
            for k in self._orig_keys:
                yield self._odx._keys_int2ext.get(k, k)

        def __reversed__(self):
            for k in reversed(self._orig_keys):
                yield self._odx._keys_int2ext.get(k, k)

    class OrderedDictXItemsView:
        def __init__(self, odx: 'OrderedDictX', orig_items):
            self._odx = odx
            self._orig_items = orig_items

        def __iter__(self):
            for k, v in self._orig_items:
                yield self._odx._keys_int2ext.get(k, k), v

        def __reversed__(self):
            for k, v in reversed(self._orig_items):
                yield self._odx._keys_int2ext.get(k, k), v

    def keys(self):
        return self.OrderedDictXKeysView(self, super().keys())

    def items(self):
        return self.OrderedDictXItemsView(self, super().items())

    def copy(self):
        return OrderedDictX(self.items())    


# FIXME: move this to pytest
if __name__ == '__main__':
    MAX = 25
    items = [(i+1, i+1) for i in range(MAX)]
    keys = [i[0] for i in items]
    d = OrderedDictX(items)

    # keys() before change
    print(list(d.items()))
    assert list(d.keys()) == keys
    # __contains__ before change
    assert 1 in d
    # __getitem__ before change
    assert d[1] == 1
    # __setitem__ before change
    d[1] = 100
    assert d[1] == 100
    d[1] = 1
    assert d[1] == 1
    # __delitem__ before change
    assert MAX in d
    del d[MAX]
    assert MAX not in d
    d[MAX] = MAX
    assert MAX in d
    print('== Tests before key change finished ==')

    # change_key and __contains__
    assert MAX-1 in d
    assert MAX*2 not in d
    d.change_key(MAX-1, MAX*2)
    assert MAX-1 not in d
    assert MAX*2 in d
    # items() and keys()
    items[MAX-2] = (MAX*2, MAX-1)
    keys[MAX-2] = MAX*2
    assert list(d.items()) == items
    assert list(d.keys()) == keys
    print(list(d.items()))
    # __getitem__
    assert d[MAX*2] == MAX-1
    # __setitem__
    d[MAX*2] = MAX*3
    items[MAX-2] = (MAX*2, MAX*3)
    keys[MAX-2] = MAX*2
    assert list(d.items()) == items
    assert list(d.keys()) == keys
    # __delitem__
    del d[MAX]
    items = items[:-1]
    keys = keys[:-1]
    assert list(d.items()) == items
    assert list(d.keys()) == keys
    d[MAX] = MAX
    items.append((MAX, MAX))
    keys.append(MAX)
    # __iter__
    assert list(d) == keys
    # __reversed__
    print(list(reversed(d.items())))
    assert list(reversed(d)) == list(reversed(keys))
    assert list(reversed(d.keys())) == list(reversed(keys))
    assert list(reversed(d.items())) == list(reversed(items))
    # pop_item()
    assert d.popitem() == (MAX, MAX)
    assert d.popitem() == (MAX*2, MAX*3)
    items = items[:-2]
    keys = keys[:-2]
    assert list(d.items()) == items
    assert list(d.keys()) == keys
    # update()
    d.update({1: 1000, MAX-2: MAX*4})
    items[0] = (1, 1000)
    items[MAX-3] = (MAX-2, MAX*4)
    assert list(d.items()) == items
    assert list(d.keys()) == keys
    # move_to_end()
    d.move_to_end(1)
    items = items[1:] + [items[0]]
    keys = keys[1:] + [keys[0]]
    assert list(d.items()) == items
    assert list(d.keys()) == keys
    # __eq__
    d.change_key(1, 2000)
    other_d = OrderedDictX(d.items())
    assert d == other_d
    assert other_d == d

