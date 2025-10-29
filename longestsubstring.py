class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        left = 0
        max_length = 0
        
        # This acts as the 'current_state' from the template
        # A set allows for O(1) addition, deletion, and lookup
        char_set = set() 

        # 1. Expand (Move 'right')
        for right in range(n):
            new_char = s[right]
            
            # 2. Check Condition & Shrink (Move 'left')
            # While the new character is already in the window (condition violated)
            while new_char in char_set:
                # Remove the character at the left pointer 
                # and slide the window to the right
                old_char = s[left]
                char_set.remove(old_char)
                left += 1
            
            # Now the condition is satisfied (new_char is not a repeat)
            # Add the new character to the set
            char_set.add(new_char)
            
            # 3. Process/Update Result
            # Current window length is (right - left + 1)
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            
        return max_length
