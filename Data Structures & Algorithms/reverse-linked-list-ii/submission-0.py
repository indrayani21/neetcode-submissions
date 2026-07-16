# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to the node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the sublist between left and right
        curr = prev.next
        nxt = None
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        # Step 3: Return the new head
        return dummy.next

        
