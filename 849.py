import sys
import collections
import functools

sys.setrecursionlimit(3000)

class memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


class Collatz:
    def __init__(self, n):
        self.n = n
        self.checked = set()
        self.probe(n)

    def next_val(self, n):
        if n <= 1:
            return 1
        elif n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1
    
    @memoize
    def validate(self, n, count=0):
        if n == 1:
            return True, count
        elif n < 1:
            return False, count
        else:
            return self.validate(self.next_val(n), count + 1)

    def probe(self, n):
        longest = (0, 0)
        failed = []
        for i in range(2, n+1):
            ok, c = self.validate(i)
            if not ok:
                print "failed " + str(i)
                failed.append(i)
            if c > longest[1]:
                longest = (i, c)
        if len(failed) == 0:
            print "all passed"
        else:
            print "failed: " + (",").join([str(i) for i in failed])
        print "longest sequence: " + str(longest)

try:
    n = int(sys.argv[1])
except ValueError:
    print "please specify a valid integer"
    exit(1)

Collatz(n)
