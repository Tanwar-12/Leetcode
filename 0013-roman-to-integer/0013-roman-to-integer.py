class Solution:
    def romanToInt(self, s):
        # Define the Roman numeral to integer mapping
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result variable
        total = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # If the current symbol is smaller than the next symbol, subtract it
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                # Otherwise, add it to the total
                total += roman[s[i]]
        
        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))     # Output: 3
print(solution.romanToInt("LVIII"))   # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994
        