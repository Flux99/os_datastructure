



def smallestsum(nums,s):
    totalsum=0
    start=0
    res = float("inf")
    for end in range(len(nums)):
        totalsum += nums[end]

        while totalsum >= s:
            res = min(end-start+1,res)
            totalsum -= nums[start]
            start+=1
    return 0 if res == float("inf") else res
    

