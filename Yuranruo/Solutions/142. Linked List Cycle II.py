#142与141很相似，区别是142要求入口node，导致直接从数据结构题变成了数学题。。。
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return
        s, f, pre=head,head,head
        while f:
            if not f.next: return

            s=s.next
            f=f.next.next
            if s==f:
                while pre!=s:
                    pre=pre.next
                    s=s.next
                return pre
        return
#贴一个大佬写的单循环代码，用了flag很巧妙
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow, res = head, head, head
        flag = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if flag: res = res.next

            if slow == fast: flag = True
            if flag and slow == res: return res
        return None