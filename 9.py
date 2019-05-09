def largest_sum_of_nonadjacent(ls):
    if len(ls) == 1:
        return ls[0]
    total = 0
    i = 0
    while i < len(ls):
        if i + 1 >= len(ls):
            total += ls[i]
            break
        left, right = ls[i], ls[i+1]
        if left > right:
            total += left
            i += 2
        else:
            next_left = 0 if i + 2 >= len(ls) else ls[i+2]
            next_right = 0 if i + 3 >= len(ls) else ls[i+3]
            if left + next_left >= right + next_right:
                total += left
                i += 2
            else:
                total += right
                i += 3
    return total


#def largest_sum_of_nonadjacent(numbers):
#    if not numbers:
#        return 0
#
#    if len(numbers) <= 2:
#        return max(numbers)
#
#    with_last = largest_sum_of_nonadjacent(numbers[:-2]) + numbers[-1]
#    without_last = largest_sum_of_nonadjacent(numbers[:-1])
#    return max(with_last, without_last)

a = [2,4,6,2,5]
s = 13
assert largest_sum_of_nonadjacent(a) == s
a = [5, 1, 1, 5]
s = 10
assert largest_sum_of_nonadjacent(a) == s
a = [12,4,2,8,10,6]
s = 26
assert largest_sum_of_nonadjacent(a) == s

import random
n = 1000000
a = []
for i in range(n):
    a.append(random.randint(0, n))
print largest_sum_of_nonadjacent(a)
