import unittest

operands = ['+', '-', '*', '/']

def calc(left:float, right:float, op:str) -> float:
    if not op in operands:
        return None
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    else:
        return left / right

def rpn(nno:list) -> int:
    stack = []
    for i in nno:
        if type(i) == int:
            stack.append(i)
        elif type(i) == str:
            r = stack.pop()
            l = stack.pop()
            stack.append(calc(l, r, i))

    return stack[0]

class TestFunc(unittest.TestCase):
    def test1(self):
        nno = [5,3,'+']
        self.assertEqual(rpn(nno), 8)

    def test2(self):
        nno = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
        self.assertEqual(rpn(nno), 5)

if __name__== "__main__":
    unittest.main()
