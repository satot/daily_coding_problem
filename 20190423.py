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

a = [1,3,5,7,9,10]
t = 17
print(pair_exists(a, t))

a = [1,3,5,7,9,10]
t = 16
print(pair_exists(a, t))

a = [1,3,5,7,9,10]
t = 20
print(pair_exists(a, t))
