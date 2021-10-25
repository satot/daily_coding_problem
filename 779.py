import unittest

def find_minimum(N:int, k:int) -> int:
    low = 0
    c = 0
    if N == 0 or k < 0:
        return 0
    if k == 1:
        return 1
    if N == 1:
        while low < k:
            low += 1
            c += 1
        return c
    if N > 1:
        return 1 + find_minimum(N-1, k//2)

class TestFunc(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_minimum(1, 5), 5)

    def test2(self):
        self.assertEqual(find_minimum(2, 5), 3)

    def test3(self):
        self.assertEqual(find_minimum(1, 1), 1)

    def test4(self):
        self.assertEqual(find_minimum(10, 3), 2)

    def test5(self):
        self.assertEqual(find_minimum(5, 4), 3)

if __name__ == "__main__":
    unittest.main()
