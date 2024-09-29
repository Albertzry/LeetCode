class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.strs = set()
        self.prev = None
        self.next = None
    
    def add(self, s):
        self.strs.add(s)
    
    def remove(self, s):
        self.strs.remove(s)

class AllOne:

    def __init__(self):
        self.nodes = dict()
        self.max = self.min = None

    def inc(self, key: str) -> None:
        if key in self.nodes:
            oldNode = self.nodes[key]
            oldNode.remove(key)
            if oldNode.next and oldNode.next.cnt == oldNode.cnt + 1:
                oldNode.next.add(key)
                self.nodes[key] = oldNode.next
            else:
                node = Node(oldNode.cnt + 1)
                if node.cnt > self.max.cnt:
                    self.max = node
                self.nodes[key] = node
                node.add(key)
                node.next = oldNode.next
                if node.next:
                    node.next.prev = node
                node.prev = oldNode
                oldNode.next = node
            if not oldNode.strs:
                if oldNode.prev:
                    oldNode.prev.next = oldNode.next
                else:
                    self.min = oldNode.next
                if oldNode.next:
                    oldNode.next.prev = oldNode.prev
                else:
                    self.max = oldNode.prev
        else:
            if self.min and self.min.cnt == 1:
                self.nodes[key] = self.min
                self.min.add(key)
            else:
                node = Node(1)
                node.add(key)
                self.nodes[key] = node
                node.next = self.min
                if self.min:
                    self.min.prev = node
                self.min = node
                if not self.max:
                    self.max = node

    def dec(self, key: str) -> None:
        oldNode = self.nodes[key]
        oldNode.remove(key)
        if oldNode.prev and oldNode.prev.cnt == oldNode.cnt - 1:
            oldNode.prev.add(key)
            self.nodes[key] = oldNode.prev
        elif oldNode.cnt > 1:
            node = Node(oldNode.cnt - 1)
            self.nodes[key] = node
            node.add(key)
            node.prev = oldNode.prev
            if node.prev:
                node.prev.next = node
            else:
                self.min = node
            node.next = oldNode
            oldNode.prev = node
        if oldNode.cnt == 1:
            self.nodes.pop(key)
        if not oldNode.strs:
            print(key)
            if oldNode.prev:
                oldNode.prev.next = oldNode.next
            else:
                self.min = oldNode.next
            if oldNode.next:
                oldNode.next.prev = oldNode.prev
            else:
                self.max = oldNode.prev

    def getMaxKey(self) -> str:
        if not self.max:
            return ""
        k = self.max.strs.pop()
        self.max.strs.add(k)
        return k

    def getMinKey(self) -> str:
        if not self.min:
            return ""
        k = self.min.strs.pop()
        self.min.strs.add(k)
        return k


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
