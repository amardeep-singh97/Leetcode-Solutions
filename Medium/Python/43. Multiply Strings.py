class Solution(object):
    def multiply(self, num1, num2):
        
        if "0" in [num1,num2]:
            return "0"
        
        res = [0]*(len(num1)+len(num2))
        i = 0
        for a in num2[::-1]:
            j = 0
            for b in num1[::-1]:
                dig = int(a)*int(b)
                res[i+j] += dig
                res[i+j+1] += res[i+j]//10 
                res[i+j] = res[i+j]%10
                j+=1
            i+=1
        
        res = res[::-1]
        pointer = 0
        
        while pointer < len(res) and res[pointer]==0:
            pointer+=1
        
        string = ""
        for i in res[pointer:]:
            string+=str(i)
        
        return string
        