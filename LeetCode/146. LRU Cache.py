"""
Design a data structure that follows the constraints of the Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of the
key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key
exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this
operation, evict the least recently used key. The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

from collections import OrderedDict
from unittest import TestCase, main


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__len = 0
        self.__q = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__q:
            self.__q.move_to_end(key)
        return self.__q.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.__q.get(key) is None:
            if self.__len == self.capacity:
                self.__q.popitem(last=False)
            else:
                self.__len += 1
        self.__q[key] = value
        self.__q.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class LRUCacheTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = LRUCache(0)

    def test_1(self):
        # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        self.obj.capacity = 2
        self.obj.put(1, 1)
        self.obj.put(2, 2)
        print(self.obj.get(1))

        self.obj.put(3, 3)
        print(self.obj.get(2))

        self.obj.put(4, 4)
        print(self.obj.get(1))
        print(self.obj.get(3))
        print(self.obj.get(4))

    def test_2(self):
        # ["LRUCache","get","put","get","put","put","get","get"]
        # [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
        # Expected output [null, -1, null, -1, null, null, 2, 6]
        self.obj.capacity = 2
        result = [
            self.obj.get(2),

            self.obj.put(2, 6),

            self.obj.get(1),

            self.obj.put(1, 5), self.obj.put(1, 2),

            self.obj.get(1), self.obj.get(2)

        ]
        self.assertEqual([-1, None, -1, None, None, 2, 6], result)


if __name__ == '__main__':
    main()
