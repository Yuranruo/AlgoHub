#解法1：迭代
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        pre=None
        cur=head
        while cur != None:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre

#解法2：递归
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None: return head
        nowNode=self.reverseList(head.next)
        head.next.next=head
        head.next=None      #因为上面是head.next.next，所以这里应当释放掉head.next
        return nowNode
#解法3：提到反转自然就有栈。。。
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        stack=[None]
        while head:
            stack.append(head)
            head=head.next
        head=stack.pop()        #先压入一个元素，不然cur及cur.next为空
        cur=head
        while stack:
            cur.next=stack.pop()
            cur=cur.next
        return head
