# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while(head is not None):
            res.append(head.val)
            head = head.next
        res.sort()
        prev =ListNode(0)
        target = prev
        for i in res:
            prev.next = ListNode(i)
            prev = prev.next
        return target.next 