# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummyHead = ListNode(0)
        # curr = dummyHead
        # carry = 0
        # while l1 != None or l2 != None or carry != 0:
        #     l1Val = l1.val if l1 else 0
        #     l2Val = l2.val if l2 else 0
        #     columnSum = l1Val + l2Val + carry
        #     carry = columnSum // 10
        #     newNode = ListNode(columnSum % 10)
        #     curr.next = newNode
        #     curr = newNode
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        # return dummyHead.next

        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            node_sum = l1_value + l2_value + carry
            carry = node_sum // 10
            ones_digit = node_sum % 10
            curr.next = ListNode(ones_digit)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next