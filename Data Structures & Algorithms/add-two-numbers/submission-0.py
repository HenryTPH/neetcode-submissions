# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        current = temp
        p1, p2 = l1, l2
        remainder = quotient = 0
        while p1 or p2 or quotient:
            val_1 = p1.val if p1 else 0
            val_2 = p2.val if p2 else 0

            total = val_1 + val_2 + quotient
            remainder = total % 10
            quotient = total // 10

            current.next = ListNode(remainder)
            current = current.next

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return temp.next