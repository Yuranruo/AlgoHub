#迭代
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        
        a=ListNode(0)
        move=a
        while l1 and l2:
            if l1.val<=l2.val:
                move.next=l1
                l1=l1.next
            else:
                move.next=l2
                l2=l2.next
            move=move.next
        if l1: move.next=l1
        else:  move.next=l2

        return a.next
#递归
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        if l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1, l2.next)
            return l2