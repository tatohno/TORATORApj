#!/usr.bin/python
# coding UTF-8
"""try property
"""

# old fashion

class UsePropertyDirectly(object):
    def __init__(self, x):
        self._x = x

    def _get_x(self):
        return self._x
    def _set_x(self, v):
        self._x = v
    def _delete_x(self):
        del self._x 
    x = property(_get_x, _set_x, _delete_x)

upd = UsePropertyDirectly(10)
print(upd.x) # getter
upd.x = 20 # setter
print(upd.x) # after using setter
del upd.x # deleter?

# new fashion

class NoProperty(object):
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x
    def set_x(self, v):
        self._x = v
    def delete_x(self):
        del self._x 
        
np = NoProperty(10)
print(np.get_x())
np.set_x(20)
np.delete_x()
