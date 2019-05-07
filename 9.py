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


a = [2,4,6,2,5]
assert largest_sum_of_nonadjacent(a) == 13
a = [5, 1, 1, 5]
assert largest_sum_of_nonadjacent(a) == 10
a = [12,4,2,8,10,6]
assert largest_sum_of_nonadjacent(a) == 26
