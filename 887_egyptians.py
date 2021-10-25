import unittest

def solve(a:int, b:int) -> list[str]:
    result = []
    i = 1
    while a > 0:
        i += 1
        if 1/i > a/b:
            continue
        a = i * a - b
        b = i * b
        result.append("1/" + str(i))
    return result

class TestFunc(unittest.TestCase):
    def test1(self):
        a = 4
        b = 13
        self.assertEqual(solve(a,b), ["1/4","1/18", "1/468"])

    def test2(self):
        a = 5
        b = 29
        self.assertEqual(solve(a,b), ["1/6", "1/174"])

    def test3(self):
        a = 1
        b = 2
        self.assertEqual(solve(a,b), ["1/2"])

if __name__ == "__main__":
    unittest.main()
