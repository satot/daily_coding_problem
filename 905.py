import unittest
from collections import defaultdict

def dfs(d: dict, start: str) -> tuple[bool, str]:
    cur = start
    while True:
        if len(d[cur]) == 0:
            break
        if len(d[cur]) == 1:
            cur = d[cur].pop()
        else:
            for c in d[cur]:
                dc = d.copy()
                dc[cur].remove(c)
                ok, cur = dfs(dc, c)
                if ok:
                    return (ok, cur)
            return (False, cur)

    return (all([len(v) == 0 for v in d.values()]), cur)

def solve(arr: list[str]) -> bool:
    if len(arr) == 0:
        return True
    if len(arr) == 1:
        return arr[0][0] == arr[0][-1]
    d = defaultdict(list)
    for c in arr:
        d[c[0]].append(c[-1])
    start = arr[0][0]
    ok, last = dfs(d, start)
    return ok and last == start

class TestFunc(unittest.TestCase):
    def test1(self):
        ls = ["chair", "height", "racket", "touch", "tunic"]
        self.assertTrue(solve(ls))

    def test2(self):
        ls = ["chair", "weight", "racket", "touch", "tunic"]
        self.assertFalse(solve(ls))

    def test3(self):
        ls = ["chair", "height", "racket", "touch", "tonight"]
        self.assertFalse(solve(ls))

if __name__ == "__main__":
    unittest.main()
