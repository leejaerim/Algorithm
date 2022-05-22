# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 1
        ans = []
        start = head
        while(not head.next == None):
            head = head.next
            cnt += 1
        val = cnt//2
        cnt = 0
        head = start
        while(not head.next == None):
            print(val, cnt)
            if val == cnt:
                return head
            head = head.next
            cnt += 1
        return head