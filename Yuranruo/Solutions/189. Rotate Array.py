#解法1：暴力删除，就是内存占用太多
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        length=len(nums)-k
        t=nums[0:length]
        del nums[0:length]
        nums += t
        #或者 nums.extend(t)
#解法2：三次翻转，先整体翻转，再以k为界两边各自翻转即可
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l += 1
                r -= 1
        length=len(nums)
        k=k%length
        reverse(0,length-k-1)
        reverse(length-k,length-1)
        reverse(0,length-1)
#解法3：环状替换，没看懂orz，下面是题解参考
#https://dwz1.cc/nBnqgnG
#https://dwz1.cc/RKeBlli
#https://dwz1.cc/7FMaBIW
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count,index,temp = 0,0,nums[0]
        done_index = [0]
        while count < len(nums):
            count,target = count+1, (index + k) % len(nums)
            temp,nums[target] = nums[target],temp
            if target not in done_index:
                index = target
            elif target + 1 < len(nums):
                index,temp = target + 1,nums[target + 1]
            done_index.append(index)