def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return helper

@memoize
def num_steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return num_steps(n-1) + num_steps(n-2)

@memoize
def num_steps_x(n, x):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sum([num_steps_x(n-i, x) for i in x])

assert num_steps(4) == 5
assert num_steps_x(4, (1,2)) == 5
assert num_steps_x(4, (1,3,5)) == 3
assert num_steps_x(5, (1,3,5)) == 5
