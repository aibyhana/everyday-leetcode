"""
1. Two Sum
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return i, j
                j = j + 1 
            i = i + 1
