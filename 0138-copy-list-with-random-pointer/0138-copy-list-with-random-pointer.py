"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copy_list = { None: None }

        current_pointer = head

        while current_pointer:
            copy_node = Node(current_pointer.val)
            copy_list[current_pointer] = copy_node
            current_pointer = current_pointer.next

        link_pointer = head
        while link_pointer:
            copy_node = copy_list[link_pointer]
            copy_node.next = copy_list[link_pointer.next]
            copy_node.random = copy_list[link_pointer.random]

            link_pointer = link_pointer.next
        
        copy_head = copy_list[head]
        return copy_head