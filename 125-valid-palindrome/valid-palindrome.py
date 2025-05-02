class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Formatting String
        if len(s) == 1:
            return True
        s = s.lower()
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c
        if len(new_s) == 1 or len(new_s) == 0:
            return True

        
        # len_s = (len(new_s)) // 2
        mid_s = (len(new_s)) // 2
        counter = 0
        for i in range (0, mid_s):
            if new_s[i] != new_s[-i-1]:
                return False
            else:
                counter += 1
        if counter > 0:
            return True 
            



        
