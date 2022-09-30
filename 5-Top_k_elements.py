# 347. Top K Frequent Elements

"""
Given an integer array nums and an integer k, return the k most 
frequent elements. 
You may return the answer in any order.
"""

# method 1
def topKFrequent(self, nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

# method 2
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    
    ans=[]
    arr=[0]*(len(nums)+1)
    
    for i in d:
        if arr[d[i]] == 0:
            arr[d[i]] = [i]
        else:
            arr[d[i]].append(i)
    
    for i in range(len(arr)-1, -1, -1):
        if len(ans) == k:
            break
        if arr[i] == 0:
            continue
        else:
            ans += arr[i]

    return ans