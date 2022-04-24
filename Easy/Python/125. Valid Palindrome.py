""" Runtime: 43 ms, faster than 74.40%
    Memory Usage: 14.2 MB, less than 71.74% """

class Solution(object):
    def isPalindrome(self, s):
        l,r=0, len(s)-1
        while(l<=r):
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True