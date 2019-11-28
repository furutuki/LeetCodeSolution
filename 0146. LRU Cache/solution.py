class ListNode:

    def __init__(self, key: int, value: int):
        """后续要根据value在字典中快速找到key，为了减少这步的时间，这里直接存了value对应的key"""
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.mapping = dict()
        self.len = 0
        self.max_size = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, item: ListNode) -> None:
        if item and item.prev != self.head:
            prev_node = item.prev
            next_node = item.next
            prev_node.next = next_node
            next_node.prev = prev_node
            item.next = self.head.next
            self.head.next.prev = item
            item.prev = self.head
            self.head.next = item

    def insert_to_head(self, new_node: ListNode) -> None:
        if not new_node:
            return
        self.len += 1
        self.head.next.prev = new_node
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node

    def get(self, key: int) -> int:
        item = self.mapping.get(key)
        if not item:
            return -1
        else:
            self.move_to_head(item)
            return item.val

    def put(self, key: int, value: int) -> None:
        item = self.mapping.get(key)
        if not item:
            """
            如果空间不够，移除tail前面的节点和它在hashmap中的key
            """
            if self.max_size == self.len:
                last_node = self.tail.prev
                last_node.prev.next = self.tail
                self.tail.prev = last_node.prev
                # del self.mapping[list(self.mapping.keys())[list(self.mapping.values()).index(last_node)]]
                del self.mapping[last_node.key]
                self.len -= 1
            """
            在head后插入新节点
            """
            new_node = ListNode(key, value)
            self.mapping[key] = new_node
            self.insert_to_head(new_node)
        else:
            item.val = value
            self.move_to_head(item)

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
