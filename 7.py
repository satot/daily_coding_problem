def memoize(f):
    cache = dict()
    def helper(s):
        if cache.get(s) is None:
            cache[s] = f(s)
        return cache[s]
    return helper
        
@memoize
def count(string):
    if len(string) == 0 or string[0] == "0":
        return 0
    if int(string) <= 26:
        return 1 + count(string[1:])
    else:
        if int(string[:2]) <= 26:
            return count(string[2:]) + count(string[1:])
        else:
            return count(string[1:])

#symbols = map(str, range(1, 27))
#@memoize
#def count(s):
#    if not s:
#        return 1
#    #matches = filter(lambda symbol: s.startswith(symbol), symbols)
#    matches = [symbol for symbol in symbols if s.startswith(symbol)]
#    print s, matches
#    encodings = [count(s[len(m):]) for m in matches]
#    return sum(encodings)

assert count('11') == 2
assert count('111') == 3
assert count('123') == 3
assert count('2626') == 4
assert count('') == 0
