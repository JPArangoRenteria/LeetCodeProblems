class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,element in enumerate(nums):
            complement = target - element
            if complement in seen:
                return [seen[complement],i]
            seen[element] = i
        return []
        
