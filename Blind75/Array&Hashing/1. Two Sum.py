"""
Runtime: 45 ms
Memory Usage: 14.2 MB
"""

class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for index,value in enumerate(nums):
            a = target - value
            if a in dic:
                return [index, dic[a]]
            dic[value] = index