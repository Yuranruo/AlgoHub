#用栈即可解决，不过两层循环的内存占用有些多。。。
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack=[]
        fakeNode=ListNode(-1)
        fakeNode.next, temp=head, head
        cur=fakeNode
        count=0
        while temp:
                count += 1
                temp=temp.next
        while head:    
            if count<k :
                fakeNode.next=head
                return cur.next
            for i in range(k):   
                stack.append(head)
                head=head.next
            count -= k
            while stack:
                fakeNode.next=stack.pop()
                fakeNode.next.next=None
                fakeNode=fakeNode.next
        return cur.next