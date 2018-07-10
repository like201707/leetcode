# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        newl = ListNode(0)
        newlc = newl
        while l1 and l2:
            if l1.val <= l2.val:
                newlc.next = l1
                l1 = l1.next
            else:
                newlc.next = l2
                l2 = l2.next
            newlc = newlc.next
        if l1:
            newlc.next = l1
        if l2:
            newlc.next = l2
        return newl.next
