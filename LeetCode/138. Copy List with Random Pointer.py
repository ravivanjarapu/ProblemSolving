"""A linked list of length n is given such that each node contains an additional random pointer, which could point to
any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the original list and copied list represent
the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val,
random_index] where:

val: an integer representing Node.val random_index: the index of the node (range from 0 to n-1) that the random
pointer points to, or null if it does not point to any node. Your code will only be given the head of the original
linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.

Hint (1/4) Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from
multiple nodes due to the random pointers, ensure you are not making multiple copies of the same node. Hint (2/4) You
may want to use extra space to keep old_node ---> new_node mapping to prevent creating multiple copies of the same
node. Hint (3/4) We can avoid using extra space for old_node ---> new_node mapping by tweaking the original linked
list. Simply interweave the nodes of the old and copied list. For example: Old List: A --> B --> C --> D InterWeaved
List: A --> A' --> B --> B' --> C --> C' --> D --> D' Hint (4/4) The interweaving is done using next pointers and we
can make use of interweaved structure to get the correct reference nodes for random pointers."""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        # # Solution with O(N) Space Complexity
        # map_dict = {None: None}
        # while cur:
        #     newNode = Node(cur.val)
        #     map_dict[cur] = newNode
        #     cur = cur.next
        #
        # cur = head
        # while cur:
        #     newNode = map_dict[cur]
        #     newNode.next = map_dict[cur.next]
        #     newNode.random = map_dict[cur.random]
        #     cur = cur.next
        # return map_dict[head]
        # # Solution with O(N) Space Complexity

        # Create new nodes and insert them in between original nodes
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode
            cur = newNode.next  # or cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Separate original nodes from new nodes
        cur = head
        newHead = head.next  # Backup to get new head later. temp will be traversed
        temp = head.next
        while cur:
            cur.next = cur.next.next
            if temp.next:
                temp.next = temp.next.next
            cur = cur.next
            temp = temp.next
        return newHead


