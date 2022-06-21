# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getValueFromList(self,targetNode:Optional[ListNode])->list:
        res = []
        if not targetNode:
            return []
        res.append(targetNode.val)
        while(not targetNode.next is None):
            targetNode= targetNode.next
            res.append(targetNode.val)
        return res
    def makeListToNode(self,targetList:list)->Optional[ListNode]:
        if not targetList:
            return None
        temp = None
        while(targetList):
            head = ListNode(targetList.pop(),temp)
            temp = head
        return head
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        targetList = self.getValueFromList(list1)+self.getValueFromList(list2)
        targetList.sort()
        return self.makeListToNode(targetList)

# brilliant answer
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()
#         while list1 and list2:               
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
                
#         if list1 or list2:
#             cur.next = list1 if list1 else list2
            
#         return dummy.next

