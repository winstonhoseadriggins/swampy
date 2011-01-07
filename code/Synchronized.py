from Queue import *

# the following is adapted from Python Cookbook page 225,
# also available at
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/65202

def _get_method_names (cls):
    import types
    
    result = []
    for name, func in cls.__dict__.items():
        if type(func) == types.FunctionType:
            result.append((name, func))

    for base in cls.__bases__:
        result.extend(_get_method_names(base))

    return result


class _SynchronizedMethod:

    def __init__ (self, method, obj, lock):
        self.__method = method
        self.__obj = obj
        self.__lock = lock

    def __call__ (self, *args, **kwargs):
        self.__lock.acquire()
        try:
            return self.__method(self.__obj, *args, **kwargs)
        finally:
            self.__lock.release()

class SynchronizedObject:
    
    def __init__ (self, obj, ignore=[], lock=None):
        self.__methods = {}
        self.__obj = obj
        lock = lock and lock or RLock()
        for name, method in _get_method_names(obj.__class__):
            if not name in ignore:
                self.__methods[name] = _SynchronizedMethod(method, obj, lock)

    def __getattr__(self, name):
        try:
            return self.__methods[name]
        except KeyError:
            return getattr(self.__obj, name)


class _QueueMethod:

    def __init__ (self, method, obj, queue):
        self.__method = method
        self.__obj = obj
        self.__queue = queue

    def __call__ (self, *args, **kwargs):
        callable = Callable(self.__method, self.__obj, *args, **kwargs)
#        self.__queue.put(callable)
        callable()


class QueueObject:
    def __init__(self, obj, methods=None):
        self.__dict__['_QueueObject__methods'] = {}
        self.__dict__['_QueueObject__obj'] = obj
        self.__dict__['_QueueObject__queue'] = Queue()

        methods = methods or _get_method_names(obj.__class__)

        import types
        for name, meth in methods:
            if type(meth) == types.FunctionType:
                self.__dict__['_QueueObject__methods'][name] = _QueueMethod(
                    meth, obj, self.__queue)

    def put(self, callable): self.__queue.put(callable)

    def get(self): return self.__queue.get_nowait()

    def __getattr__(self, name):
        try:
            return self.__methods[name]
        except KeyError:
            return getattr(self.__obj, name)

    def __setattr__(self, name, value):
        setattr(self.__obj, name, value)
