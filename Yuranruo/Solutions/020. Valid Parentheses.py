#直接用栈即可
class Solution1:
    def isValid(self, s: str) -> bool:
        stack=[]
        i=-1
        for t in s:
            stack.append(t)
            if (t==")" and stack[i]=="(") or (t=="]" and stack[i]=="[") or (t=="}" and stack[i]=="{"):
                stack.pop()
                stack.pop()
                i-=2
            i+=1
        return not stack