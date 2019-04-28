import unittest
# input1: list(num) [1,3,5,7,9,10]
# input2: num 17
# output: bool True/False


def pair_exists(candidates, target):
    memo = dict()
    for n in candidates:
        if memo.get(n):
            return True
        memo[target - n] = target - n
    return False


class TestFunc(unittest.TestCase):
    def test1(self):
        a = [1,3,5,7,9,10]
        t = 17
        self.assertTrue(pair_exists(a, t))

    def test2(self):
        a = [1,3,5,7,9,10]
        t = 16
        self.assertTrue(pair_exists(a, t))

    def test3(self):
        a = [1,3,5,7,9,10]
        t = 20
        self.assertFalse(pair_exists(a, t))

    def test4(self):
        a = [10,9,1,3,4,2]
        t = 5
        self.assertTrue(pair_exists(a, t))

unittest.main()
