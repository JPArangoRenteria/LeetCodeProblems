class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(0,len(nums)):
            for j in range(i, len(nums)):
                if i+k <= len(nums):
                    sub = nums[i:i+k]
                    for l in range(1,len(sub)):
                        if sub[l-1] >= sub[l]:
                            return False
                    return True
