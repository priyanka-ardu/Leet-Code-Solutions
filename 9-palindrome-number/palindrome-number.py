class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)[::-1]
        if x1 == str(x):
            return True
        else: 
            return False


        
        