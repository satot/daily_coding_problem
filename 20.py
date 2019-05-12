class LinkedListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

def get_length(n):
    if n is None:
        return 0
    length = 1
    while n.next:
        length += 1
        n = n.next
    return length

def find_intersect(a, b):
    len_a = get_length(a)
    len_b = get_length(b)
    if a == 0 or b == 0:
        return None
    length = min(len_a, len_b)
    if len_a > len_b:
        for _ in range(len_a - len_b):
            a = a.next
    elif len_b > len_a:
        for _ in range(len_b - len_a):
            b = b.next
    for _ in range(length):
        if a.next is None or b.next is None:
            return None
        if a.next.val == b.next.val:
            return a.next.val
        a, b = a.next, b.next
    return None


c = LinkedListNode(8, LinkedListNode(10))
a = LinkedListNode(3, LinkedListNode(7, c))
b = LinkedListNode(99, LinkedListNode(1, c))
assert find_intersect(a, b) == 8

c = LinkedListNode(8, LinkedListNode(7))
a = LinkedListNode(5, LinkedListNode(2, LinkedListNode(1, c)))
b = LinkedListNode(6, c)
assert find_intersect(a, b) == 8
