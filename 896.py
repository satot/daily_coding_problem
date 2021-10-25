import unittest

# m > 0, n > 0
def divide(m:int, n:int) -> int:
    i = 0
    while m >= n:
        m -= n
        i += 1
    return i

class TestFunc(unittest.TestCase):
    def test1(self):
        m, n = 4, 2
        self.assertEqual(divide(m, n), m//n)

    def test2(self):
        m, n = 213210909, 324324
        self.assertEqual(divide(m, n), m//n)

    def test3(self):
        m, n = 332432897912321987953, 29384732984723
        self.assertEqual(divide(m, n), m//n)

if __name__ == "__main__":
    unittest.main()
