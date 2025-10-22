class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the symbols and their values, sorted in descending order
        mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_numeral = ""
        
        for value, symbol in mapping:
            # Count how many times the value fits into the remaining number
            count = num // value
            
            # Append the symbol 'count' times
            roman_numeral += symbol * count
            
            # Subtract the total value from the number
            num -= value * count
            
            # Optimization: If the number is zero, we are done
            if num == 0:
                break
                
        return roman_numeral
