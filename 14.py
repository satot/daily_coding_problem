from random import randint

# Monte Carlo method
# a = (pi * r^2) / (2r * 2r)
#   = pi / 4
# i.e. pi = 4 * a
def find_a(n):
    inner = 0
    for i in range(n):
        x, y = randint(-n, n), randint(-n, n)
        if x ** 2 + y ** 2 <= n ** 2:
            inner += 1
    return float(inner)/n

def find_pi(n):
    return 4 * find_a(n)

print find_pi(1000000)
