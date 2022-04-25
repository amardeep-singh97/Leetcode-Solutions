"""
Runtime: 68 ms, faster than 35.33% of Python online submissions for Valid Anagram.
Memory Usage: 16.6 MB, less than 5.22% of Python online submissions for Valid Anagram.
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        lis1=[]
        lis2=[]
        for i in range(len(s)):
            lis1.append(s[i])
            lis2.append(t[i])
        lis1.sort()
        lis2.sort()
        
        return lis1==lis2

#Second Solution

