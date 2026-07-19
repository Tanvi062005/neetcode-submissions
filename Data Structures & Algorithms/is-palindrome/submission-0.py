class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 #left points to 0th index and right points to the last character
        
        while left < right: # This loop controls the entire algorithm.
            while left < right and not s[left].isalnum(): # This one is for skipping invalid characters.
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): #.lower() lowers all the characters
                return False
            
            left += 1
            right -= 1

        return True
