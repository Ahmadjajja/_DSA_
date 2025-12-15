class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)

        self.head.next, self.tail.prev = self.tail, self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next = next
        next.prev = prev

    def insert(self, node):
        next, prev = self.tail, self.tail.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)