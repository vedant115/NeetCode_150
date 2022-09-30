# Leetcode - 217. 
# Contains Duplicate

"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

# method 1
def containsDuplicate(nums):
    d={}
    for num in nums:
        d[num] = d.get(num, 0) + 1
        if d[num] > 1:
            return True
    return False

# method 2
def containsDuplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False

# method 3
def containsDuplicate(nums):
    return len(nums) != len(set(nums))