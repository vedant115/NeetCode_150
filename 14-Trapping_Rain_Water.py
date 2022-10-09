# 42. Trapping Rain Water

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""

# method 1
def trap(height):
    n=len(height)
    l, r = 0, n-1
    maxLeft=[0]*n
    maxRight=[0]*n
    ml, mr = 0, 0
    while l < n:
        ml = max(ml, height[l])
        mr = max(mr, height[r])
        maxLeft[l] = ml
        maxRight[r] = mr
        l+=1
        r-=1
    ans=0
    for i in range(n):
        m = min(maxLeft[i], maxRight[i])
        ans+=(m-height[i])
    return ans

# method 2
def trap(height):
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res