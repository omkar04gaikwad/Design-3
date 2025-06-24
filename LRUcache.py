# """
# Approach:
# - Use a combination of a Doubly Linked List and a Hash Map (dictionary) to achieve O(1) time for both get and put operations.
# - The Doubly Linked List maintains the usage order — most recently used (MRU) node is near the head, least recently used (LRU) near the tail.
# - The Hash Map maps keys to nodes in the DLL for O(1) access.

# Operations:
# - get(key): If key exists, move node to head (mark as most recently used) and return its value.
# - put(key, val): If key exists, update value and move to head.
#                 If not, insert new node at head. If over capacity, remove LRU node from tail.

# Time Complexity:
# - get: O(1)
# - put: O(1)

# Space Complexity:
# - O(capacity) for both the cache dict and the doubly linked list nodes.
# """
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next.prev = node
        else:
            node = Node(key, value)
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next.prev = node
            self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            lru.prev.next = self.tail
            self.tail.prev = lru.prev
            lru.prev = lru.next = None
            del self.cache[lru.key]

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # Returns 1
    lru.put(3, 3)        # Evicts key 2
    print(lru.get(2))    # Returns -1 (not found)
    lru.put(4, 4)        # Evicts key 1
    print(lru.get(1))    # Returns -1 (not found)
    print(lru.get(3))    # Returns 3
    print(lru.get(4))    # Returns 4

