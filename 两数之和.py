class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l={}
        for i,num in enumerate(nums):
            if target-num in l:
                return l[target-num],i
            l[num]=i