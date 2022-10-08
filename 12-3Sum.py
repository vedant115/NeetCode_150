# 15. 3Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums):
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum > 0:
                    r-=1
                elif curSum < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res