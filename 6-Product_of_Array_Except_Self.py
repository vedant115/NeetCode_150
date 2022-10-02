# 238. Product of Array Except Self

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# method 1
def productExceptSelf(nums):
    pre = [0]*len(nums)
    post = [0]*len(nums)
    ans = [0]*len(nums)
        
    prod = 1
    pre[0] = 1
    for i in range(1, len(nums)):
        prod*=nums[i-1]
        pre[i]=prod

    prod=1
    post[-1]=1
    for i in range(len(nums)-2, -1, -1):
        prod*=nums[i+1]
        post[i]=prod
            
    for i in range(len(nums)):
        ans[i] = pre[i]*post[i]
        
    return ans

# method 2
def productExceptSelf(nums):
    ans = [1]*len(nums)
        
    prefix=1
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]
        
    postfix=1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
            
    return ans