import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1= s.lower()
        s2 = s1.strip(" ")
        s3 = s2.replace(" ","")
        s4 = s3.translate(str.maketrans("", "", string.punctuation))
        print(s4)
        left = 0 
        right = len(s4)-1
        while left <= right:
            if s4[left] != s4[right]:
                return False
            if s4[left] != s4[right] and left == right:
                return False
            left += 1
            right -= 1
        return True
        