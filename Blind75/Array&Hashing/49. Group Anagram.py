class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs)==1:
            return [strs]
        
        dic = {}
        
        for string in strs:
            key = "".join(sorted(string))
            
            if key not in dic:
                dic[key] = [string]
            else:
                dic[key].append(string)
            
        
        return dic.values()
