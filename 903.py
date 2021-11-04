import unittest

def twoSum(arr: list[int], k:int) -> bool:
    if len(arr) < 2:
        return False
    memo = dict()
    for n in arr:
        if n in memo:
            return True
        memo[k-n] = 1
    return False

def solve(arr: list[int], k:int) -> bool:
    for i in range(len(arr) - 1):
        if twoSum(arr[i+1:], k-arr[i]):
            return True
    return False

class TestFunc(unittest.TestCase):
    def test1(self):
        inp = [20, 303, 3, 4, 25]
        k = 49
        self.assertTrue(solve(inp, k))

    def test2(self):
        inp = [20, 303, 3, 4, 25]
        k = 32
        self.assertTrue(solve(inp, k))

if __name__ == "__main__":
    unittest.main()
