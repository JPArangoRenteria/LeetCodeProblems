class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sumres = []
        for i in range(0,len(nums)):
            curr = nums[i]
            for j in range(i,len(nums)):
                for k in range(1,len(nums)-1):
                    add = curr+sum(nums[j:k])
                    sumres.append(add)
        diff = 0
        counter = 0
        print(sumres)
        abs_list = []
        for l in range(0,len(sumres)):
            abs_list.append(abs(target-sumres[l]))
        if target in abs_list:
            pass
        else:
            i = abs_list.index(min(abs_list))
        return sumres[i]
