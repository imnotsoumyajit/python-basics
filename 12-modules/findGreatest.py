def findGreatest(nums):
    i=0
    gn=nums[0]
    for i in nums:
        if(i>gn):
            gn=i
    return gn