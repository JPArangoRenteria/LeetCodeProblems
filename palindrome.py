class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = len(s)
        return (s == s[::-1])
