""" Runtime: 510 ms, faster than 41.30% of Python online submissions for Contains Duplicate.
    Memory Usage: 24.1 MB, less than 22.79% of Python online submissions for Contains Duplicate.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        a = set(nums)
        return not len(a)==len(nums)

#Second Solution

"""
Runtime: 537 ms, faster than 35.37% of Python online submissions for Contains Duplicate.
Memory Usage: 22.5 MB, less than 92.28% of Python online submissions for Contains Duplicate.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False