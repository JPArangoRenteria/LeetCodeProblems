class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 3:
            triplet_acc = []
            for i in range(0,len(nums)):
                for j in range(i+1,len(nums)):
                    for k in range (j+1,len(nums)):
                        if (nums[i] + nums[j] + nums[k]) == 0:
                            inner = [nums[i],nums[j],nums[k]]
                            inner = sorted(inner)
                            print(inner)
                            #triplet_acc.append([nums[i],nums[j],nums[k]])
                            triplet_acc.append(inner)
            seen = set()
            result = []
            print(triplet_acc)
            for l in range(0, len(triplet_acc)):
                t = tuple(triplet_acc[l])
                print(t)
                print(seen)
                if t not in seen:
                    seen.add(t)
                    result.append(triplet_acc[l])
            triplet_acc = result
            return triplet_acc
        else:
            if len(nums) == 3:
                if (nums[0]+nums[1]+nums[2]) == 0:
                    return [[nums[0],nums[1],nums[2]]]
                else:
                    return []
            else:
                return []
