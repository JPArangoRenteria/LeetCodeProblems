class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        ws = tuple(dict(enumerate(s)).values())
        d = {}
        for w in ws:
            c = s.count(w)
            d[w] = c
        ks = d.keys()
        vs = d.values()
        max_odd = max(num for num in vs if num %2 != 0)
        min_even = min(num for num in vs if num %2 == 0)
        return max_odd-min_even
            
