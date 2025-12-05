
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_end = end
        self.left: Node = None
        self.right: Node = None

class IntervalTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, start, end):
        if not self.root:
            self.root = Node(start, end)
        else:
            self._insert(self.root, start, end)
    
    def _insert(self, node: Node, start, end):
        node.max_end = max(node.max_end, end)

        if start < node.start:
            if node.left: self._insert(node.left, start, end)
            else: node.left = Node(start, end)
        else:
            if node.right: self._insert(node.right, start, end)
            else: node.right = Node(start, end)
    
    def contains(self, value: int):
        return self._contains(self.root, value)
    
    def _contains(self, node: Node, value):
        if not node:
            return False
        
        if node.start <= value <= node.end:
            return True
        
        if node.left and node.left.max_end >= value:
            return self._contains(node.left, value)
        
        if node.start <= value:
            return self._contains(node.right, value)
        return False


with open("data/input_5.txt", "r") as file:
    tree = IntervalTree()
    while (line := file.readline()) != '\n':
        a, b = line.strip().split('-')
        tree.insert(int(a), int(b))

    res = 0
    for line in file:
        res += tree.contains(int(line))
print(res)