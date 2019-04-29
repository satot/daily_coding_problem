from Queue import Queue

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    to_check = Queue()
    to_check.put(root)
    result = []
    while not to_check.empty():
        node = to_check.get()
        if node:
            result.append(node.val)
            to_check.put(node.left)
            to_check.put(node.right)
        else:
            result.append(None)
    return repr(result)


def deserialize(string):
    ls = eval(string)
    root = ls.pop(0)
    if not root:
        return None
    root_node = Node(root)
    to_check = Queue()
    to_check.put(root_node)
    while not to_check.empty():
        node = to_check.get()
        left = ls.pop(0)
        if left:
            node.left = Node(left)
            to_check.put(node.left)
        right = ls.pop(0)
        if right:
            node.right = Node(right)
            to_check.put(node.right)
    return root_node



try:
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert serialize(node) == "['root', 'left', 'right', 'left.left', None, None, None, None, None]"
    assert deserialize(serialize(node)).left.left.val == 'left.left'

    node = None
    #assert serialize(node) == "[None]"
    #assert deserialize(serialize(node)) is None

    print "Test success!"
except Exception as e:
    print "Test fail"
    print e