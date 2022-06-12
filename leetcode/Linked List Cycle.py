# Linked List Cycle
# My Answer :
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        buffer = []
        temp = head
        if head == None :
            return False
        while(temp.next != None):
            if temp in buffer:
                return True
            buffer.append(temp)
            temp = temp.next


#Best Answer i think :
# Becuase of Using Dictionary in that case this guy already knows visited dictionary's key is Object
# that's why no duple in dictionary

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = {}
        
#         while head:
#             if head.next in visited:
#                 return True
            
#             visited[head] = True
#             head = head.next
            
#         return False