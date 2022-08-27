# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        if head is None :
            return None
        res.val = head.val
        if head.next == None :
            return res
        while(head.next != None):
            head = head.next
            temp = ListNode()
            temp.val = head.val
            temp.next = res
            res = temp
        return temp

# Best Answer i think :
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next:
#             return head
        
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# second answer
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return None
        _list = []
        next_to_go = None
        while(head is not None):
            _list.append(head)
            head = head.next
        head = None
        while(_list):
            temp = _list.pop()
            if head is None:
                head = temp
                prev = temp
            else:
                prev.next = temp
                prev = temp
        temp.next = None
        return head