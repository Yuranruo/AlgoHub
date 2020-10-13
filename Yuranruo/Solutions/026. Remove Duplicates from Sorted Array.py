#题目描述中有个tip：“根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。”，意味着并不需要真的删除元素，只需要保证前i+1项是正确答案即可
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<1: return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i]=nums[j]
        return i+1