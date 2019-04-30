class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_tree(node):
    (total_count, is_unival) = helper(node)
    return total_count

def helper(node):
    if not node:
        return (0, True)
    (left_count, is_left_unival) = helper(node.left)
    (right_count, is_right_unival) = helper(node.right)
    is_unival = True
    if node.left and (node.left.val != node.val):
        is_unival = False
    if node.right and (node.right.val != node.val):
        is_unival = False
    if is_unival and is_left_unival and is_right_unival:
        return (left_count + right_count + 1, True)
    else:
        return (left_count + right_count, False)

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
assert count_unival_tree(root) == 5
root = Node(1, Node(1), Node(1, Node(1, Node(1), Node(1)), Node(1)))
assert count_unival_tree(root) == 7
root = Node(1, Node(1), Node(1, Node(1, Node(1), Node(0)), Node(1)))
assert count_unival_tree(root) == 4
