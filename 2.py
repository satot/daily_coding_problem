import unittest

# input: list(num) [1,2,3,4,5]
# output: new list(num) [120, 60, 40, 30, 24]

def power(ls):
    p = 1
    zero_count = 0
    for n in ls:
        if n == 0:
            zero_count += 1
        else:
            p *= n
    result = []
    if zero_count > 1:
        result = [0] * len(ls)
    elif zero_count == 1:
        for n in ls:
            if n == 0:
                result.append(p)
            else:
                result.append(0)
    else:
        for n in ls:
            result.append(p/n)
    return result


class TestFunction(unittest.TestCase):
    def test1(self):
        a = [1,2,3,4,5]
        self.assertEqual(power(a), [120, 60, 40, 30, 24])

    def test2(self):
        a = [3,2,1]
        self.assertEqual(power(a), [2,3,6])

    def test3(self):
        a = [0,2,4]
        self.assertEqual(power(a), [8,0,0])

    def test4(self):
        a = [4,1,0,-1]
        self.assertEqual(power(a), [0,0,-4,0])

    def test5(self):
        a = [0,2,0]
        self.assertEqual(power(a), [0,0,0])

if __name__ == '__main__':
    unittest.main()

