class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        l1 = headA
        l2 = headB
        
        while l1 != l2:
            if l1 is not None:
                l1 = l1.next
            else:
                l1 = headB

            if l2 is not None:
                l2 = l2.next
            else:
                l2 = headA
        return l1