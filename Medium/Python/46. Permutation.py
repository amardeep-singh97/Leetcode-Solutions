def permute(nums):
    n=len(nums)
    stack=[False for i in range(n)]
    res= []
    def backtrack(track):
        if len(track)==n:
            res.append(track)
            return
        for i in range(n):
            if stack[i]:
                continue
            stack[i]=True
            backtrack(track+[nums[i]])
            stack[i]=False
    backtrack([])
    return res

print(permute([1,2,3]))     