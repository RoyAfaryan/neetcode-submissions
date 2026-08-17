class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        copy = s.replace(" ", "").lower()
        copy = "".join(char for char in copy if char.isalnum())
      
        for i in range(len(copy)):
            if copy[i] != copy[-i-1]:
                return False
        
        return True
        