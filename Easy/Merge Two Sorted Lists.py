class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        res = result
        while l1 and l2:
            if l1.val < l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next
            
        if l1:
            res.next = l1
        else:
            res.next = l2
            
        return result.next
