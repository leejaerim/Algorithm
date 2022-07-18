# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        nxt = None
        cnt = 0 
        head = None
        chk = False
        cnt = 0
        while l1 is not None or l2 is not None or cnt == 1:
            if l1 is None and l2 is None and cnt == 1:
                prev.next = ListNode(1,None)
            tmp1, tmp2 = 0, 0
            if l1 is not None:
                tmp1 = l1.val
                l1 = l1.next
            if l2 is not None:
                tmp2 = l2.val
                l2 = l2.next
            tmp = tmp1 + tmp2 + cnt
            if  tmp >=10:
                tmp -= 10
                chk = True
            if prev is None:
                prev = ListNode(tmp,None)
                cnt = 0
                head = prev
            else:
                nxt = ListNode(tmp,None)
                cnt = 0
                prev.next = nxt
                prev = nxt 
            if chk :
                cnt += 1
                chk = False
        return head