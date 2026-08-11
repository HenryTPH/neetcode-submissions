# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        previous = None
        while current:
            # Save the next node
            next = current.next
            # Point the current.next to previous
            current.next = previous
            # Move the previous to current position
            previous = current
            # Move current to next
            current = next
        return previous