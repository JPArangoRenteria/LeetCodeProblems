class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = []
        def isPalindrome(s):
            return s == s[::-1]
        if len(s) <= 1:
            palindromes.append(s)
        elif s == s[::-1]:
            return s
        elif isPalindrome(s):
            palindromes.append(s)
        print(palindromes)
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                if isPalindrome(substr):
                    palindromes.append(substr)
       
        palindrome = ''
        print(palindromes)
        for k in range(0,len(palindromes)):
            if len(palindromes[k]) > len(palindrome):
                palindrome  = palindromes[k]
            else: 
                continue
        return palindrome
                        

