# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        memo = set([])
        prev = None
        while(head):
            if head.val in memo and prev is not None:
                prev.next = head.next
            else:
                memo.add(head.val)
                prev = head
            if head.next is None:
                    break
            else:
                head = head.next
        return start