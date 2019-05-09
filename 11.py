from bisect import bisect_left as bisect

def autocomplete(query, candidates):
    return [w for w in candidates if w.startswith(query)]

def autocomplete2(query, candidates):
    dictionary = [s.lower() for s in sorted(candidates)]
    next_query = query + 'a' if query[-1] == 'z' else query[:-1] + chr(ord(query[-1]) + 1)
    return dictionary[bisect(dictionary, query):bisect(dictionary, next_query)]


s = "de"
c = ["dog", "deal", "deer"]
assert autocomplete(s, c) == ["deal", "deer"]
assert autocomplete2(s, c) == ["deal", "deer"]
