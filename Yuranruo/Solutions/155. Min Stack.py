#大水题。。。就是让你手动实现一个栈，加上获取最小值的方法
class MinStack_false:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        del self.items[len(self.items)-1]

    def top(self) -> int:
        return self.items[len(self.items)-1]

    def getMin(self) -> int:
        return min(self.items)


#眼瞎，才发现要在常数时间内实现
class MinStack_true:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.items=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.items or x<=self.items[-1]: #-1就是列表中最后一个元素，即栈顶
            self.items.append(x)
    def pop(self) -> None:
        if self.stack.pop()==self.items[-1]:
            self.items.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.items[-1]