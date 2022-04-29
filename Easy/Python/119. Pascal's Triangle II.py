"""
Runtime: 17 ms, faster than 83.95% of Python online submissions for Pascal's Triangle II.
Memory Usage: 13.3 MB, less than 67.04% of Python online submissions for Pascal's Triangle II.
"""
class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        
        res= [[1]]
        
        for i in range(2,rowIndex+2):
            sudo = res[0]*i
            if i>2:
                for r in range(len(res[i-2])-1):
                    sudo[r+1] = res[i-2][r] + res[i-2][r+1]
                    
            res.append(sudo)
        
        return res[rowIndex]