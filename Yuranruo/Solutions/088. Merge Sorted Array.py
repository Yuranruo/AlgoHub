#直接合并+sort即可。。。
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums1[:m]+nums2    #为何要用nums1[:]，这个解释的很清楚：https://dwz1.cc/7ewH9Bw
        nums1.sort()
#双指针法，利用nums1的空间从后往前推，从而空间复杂度为O(1)
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                i-=1
            k-=1
        nums1[:j+1]=nums2[:j+1]