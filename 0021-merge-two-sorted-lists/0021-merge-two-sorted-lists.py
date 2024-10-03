# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged_list = ListNode()
        current_pointer = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                current_pointer.next = list1
                list1 = list1.next

            else:
                current_pointer.next = list2
                list2 = list2.next
            
            current_pointer = current_pointer.next

        current_pointer.next = list1 if list1 else list2

        return merged_list.next