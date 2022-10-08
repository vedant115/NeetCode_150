# 11. Container With Most Water

"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

# method 1 (brute force-O(n^2))
def maxArea(height):
    ans=0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = (r-l)*min(height[l], height[r])
            ans=max(ans, area)
    return ans

# method 2 O(n)
def maxArea(height):
    ans=0
    l, r = 0, len(height)-1
    while l < r:
        area = (r-l)*min(height[l], height[r])
        ans=max(ans, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans

# method 3 (optimized)
def maxArea(height):
    l, r, ans = 0, len(height) - 1, 0
    while l < r:
        min_height=min(height[l], height[r])
        ans = max(ans, (r - l) * min_height)
        if height[l] < height[r]:
            l+=1
            while height[l]<min_height:
                l+=1
        else:
            r-=1
            while height[r]<min_height:
                r-=1
    return ans