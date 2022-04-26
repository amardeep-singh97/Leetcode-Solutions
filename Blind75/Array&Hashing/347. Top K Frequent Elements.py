"""
Runtime: 168 ms, faster than 18.01% of Python online submissions for Top K Frequent Elements.
Memory Usage: 16.9 MB, less than 54.59% of Python online submissions for Top K Frequent Elements.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums)==1:
            return nums
        dic = {}
        for i in nums:
            dic[i] = 1 + dic.get(i,0)
        
        res = []
        for _ in range(k):
            maxi = 0
            val = -1
            for key,value in dic.items():
                if value>maxi:
                    maxi=value
                    val = key
            res.append(val)
            dic.pop(val)
        return res