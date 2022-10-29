# 239. Sliding Window Maximum

"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

from collections import deque 
def maxSlidingWindow(nums, k):
    ans = []
    q = deque()
    i, j = 0, 0
    while j < len(nums):
        while q and q[-1] < nums[j]:
            q.pop()
        q.append(nums[j])
        if j-i+1 < k:
            j += 1
        elif j-i+1 == k:
            ans.append(q[0])
            if nums[i] == q[0]:
                q.popleft()
            i += 1
            j += 1
    return ans