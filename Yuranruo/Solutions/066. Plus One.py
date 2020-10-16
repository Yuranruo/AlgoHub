#将数组转化为int整数，直接+1再取余到数组中
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int("".join([str(t) for t in digits]))
        a+=1
        i=len(str(a))-1
        nums=[0]*(i+1)
        while a>=1:
            nums[i]=a%10
            a=a//10
            i-=1
        return nums
#最直观的，判断每一位是否为9，不是的话直接再最高位+1输出即可，不过要注意类似999的edge case
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] is not 9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                if digits[0]==0:
                    digits.insert(0, 1)
                    return digits