# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the k-th node
            kth = group_prev
            for _ in range(k):
                if not kth:
                    break
                kth = kth.next
            
            # If we don't have enough nodes to reverse, we are done
            if not kth:
                break

            # Pointers for reversal
            group_start = group_prev.next
            group_next = kth.next

            # Reverse the k nodes
            reverse(group_start, group_next)

            # Reconnect the reversed group
            group_prev.next = kth
            group_start.next = group_next

            # Move group_prev to the tail of the current reversed group
            group_prev = group_start

        return dummy.next