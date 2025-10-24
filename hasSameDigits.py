class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        else:
            n = len(s)
            m = ""
            for i in range(0,n-1):
                m = m + str((int(s[i])+int(s[i+1]))%10)
            return self.hasSameDigits(m)
                
