""" Runtime: 28 ms, faster than 30.44% 
    Memory Usage: 13.3 MB, less than 86.92% 
    NOTE: ROOM for improvement in runtime"""

class Solution(object):
    
    def generate(self, numRows):
        if numRows==1:
            return [[1]]
        
        res= [[1]]
        
        for i in range(2,numRows+1):
            sudo = res[0]*i
            if i>2:
                for r in range(len(res[i-2])-1):
                    sudo[r+1] = res[i-2][r] + res[i-2][r+1]
                    
            res.append(sudo)
        
        return res