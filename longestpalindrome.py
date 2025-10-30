class Solution(object):
    def expand(self,s, left, right):
        # This loop expands the window (left, right) as long as:
        # 1. The boundaries (left, right) are within the string limits.
        # 2. The characters at those boundaries match.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # When the loop breaks, 'left' and 'right' are one step *past* # the actual boundaries of the longest palindrome.
        
        # The length of the palindrome is: (right_index - left_index + 1)
        # The actual indices were: (left + 1) and (right - 1).
        # Length = (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        # 1. Initialization for tracking the best result
        max_length = 0
        start_index = 0
        
        # Optional: You can embed the expand function inside or call a standalone one
        # For simplicity, let's assume the expand function from above is available.
        
        # 2. Iterate through every character as a potential center
        for i in range(len(s)):
            
            # Case A: Odd-length palindrome (Center is s[i])
            # Start expansion from (i, i)
            len1 = self.expand(s, i, i)
            
            # Case B: Even-length palindrome (Center is between s[i] and s[i+1])
            # Start expansion from (i, i+1)
            len2 = self.expand(s, i, i + 1)
            
            # 3. Determine the longest palindrome found from this center
            current_max_len = max(len1, len2)
            
            # 4. Update the overall best result
            if current_max_len > max_length:
                max_length = current_max_len
                
                # The start index calculation is the trickiest part:
                # We started at 'i', and expanded outwards by an equal amount on both sides.
                # To get the start index, you take the center 'i' and move back half the length.
                # Use integer division // for the correct shift.
                start_index = i - (max_length - 1) // 2

        # 5. Return the substring based on the best indices found
        return s[start_index : start_index + max_length]

# Note: You must place the 'expand' helper function so it's accessible.

            
