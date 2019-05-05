#def first_missing_positive(digits):
#    digits.sort() # O(n*log(n))
#    missing = 1
#    for n in digits: # O(n)
#        if n <= 0:
#            continue
#        if n > missing:
#            return missing
#        else:
#            missing = n + 1
#    return missing

def first_missing_positive(digits):
    max_d = max(digits) #O(n)
    count = dict()
    for n in digits: #O(n)
        if count.get(n):
            count[n] += 1
        else:
            count[n] = 1
    if len([n for n in count.keys() if n > 0]) == max_d: #O(n)
        return max_d + 1
    for n in range(1, max_d + 1): #O(n)
        if count.get(n):
            continue
        return n
        

a = [3, 4, -1, 1]
assert first_missing_positive(a) == 2

a = [1, 2, 0]
assert first_missing_positive(a) == 3

a = [4, -1, 1, 1, 2]
assert first_missing_positive(a) == 3

a = [-1, -3, 0, -2]
assert first_missing_positive(a) == 1

a = [-1, -3, 1, -2]
assert first_missing_positive(a) == 2

a = [-1, -3, 2, -2]
assert first_missing_positive(a) == 1

n = 1000000
import random
a = []
for i in range(n):
    a.append(random.randint(0, n))
#assert first_missing_positive(a) == n
first_missing_positive(a)
