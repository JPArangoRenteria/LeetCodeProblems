class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        queue = s[0]
        result = []
        for i in range(1,len(s)):
            if not(s[i] in queue):
                queue = queue + s[i]
                print(queue)
            else:
                print(len(queue))
                result.append(len(queue))
                queue = s[i]
               #return(len(queue))
        if len(queue) == len(s):
            return len(queue)
        print(result)
        return max(result,default = 0)
