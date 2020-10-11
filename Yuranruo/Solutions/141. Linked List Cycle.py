#解法一：快慢指针
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        s=head
        f=head.next
        while s!=f:
            if f is None or f.next is None:
                return False
            s=s.next
            f=f.next.next 
        return True
#解法二：翻转链表————链表过程中，如果有环则会回到head节点
#解法三：删除链表节点，如果有环则存在head=head.next