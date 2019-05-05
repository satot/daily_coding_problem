class XorLinkedListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.both = prev ^ next

    def next_node(self, prev_index):
        return self.both ^ prev_index

    def prev_node(self, next_index):
        return self.both ^ next_index


class XorLinkedList:
    def __init__(self):
        self.memory = [XorLinkedListNode(None, -1, -1)]

    # head node index,
    # prev node index,
    # head node
    def head(self):
        return 0, -1, self.memory[0]

    def add(self, val):
        current_node_idx, prev_node_idx, current_node = self.head()
        while True:
            next_node_idx = current_node.next_node(prev_node_idx)
            if next_node_idx == -1:
                break
            prev_node_idx, current_node_idx = current_node_idx, next_node_idx
            current_node = self.memory[next_node_idx]

        new_node_idx = len(self.memory)
        current_node.both = prev_node_idx ^ new_node_idx
        self.memory.append(XorLinkedListNode(val, current_node_idx, -1))

    def get(self, idx):
        current_node_idx, prev_node_idx, current_node = self.head()
        while current_node_idx != idx:
            next_node_idx = current_node.next_node(prev_node_idx)
            prev_node_idx, current_node_idx = current_node_idx, next_node_idx
            current_node = self.memory[next_node_idx]
        return self.memory[current_node_idx+1]


xll = XorLinkedList()
xll.add(3)
xll.add(2)
xll.add(4)
xll.add(1)

assert xll.get(3).val == 1

l = XorLinkedList()
for c in xrange(0,4):
    l.add(c)
assert l.get(2).val == 2
