# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        count = 0
        current_ptr = head
        while current_ptr:
            count += 1
            current_ptr = current_ptr.next
        
        middle_index = (count // 2) + 1
        
        counter = 1
        mid_ptr = head
        while counter != middle_index:
            counter += 1
            mid_ptr = mid_ptr.next

        return mid_ptr