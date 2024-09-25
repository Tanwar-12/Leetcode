# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val>l2.val:
            l1,l2=l2,l1
        head = l1
        while(l1!=None and l2!=None):
            if l1.next==None:
                l1.next=l2
                return head
            if l1.val <= l2.val and l1.next.val>=l2.val:
                l2.next,l1.next,l2=l1.next,l2,l2.next
            l1=l1.next
        return head