# Leetcode - 242. 
# Valid Anagram

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

# method 1
def isAnagram(self, s: str, t: str) -> bool:
    
    if len(s) != len(t):
        return False
    
    ds=dict()
    dt=dict()
    
    for i in range(len(s)):
        ds[s[i]] = ds.get(s[i], 0) + 1
        dt[t[i]] = dt.get(t[i], 0) + 1
        
    return (ds == dt)

# method 2
from collections import defaultdict
def isAnagram(self, s: str, t: str) -> bool:
    tracker = defaultdict(int)
    for x in s: tracker[x] += 1
    for x in t: tracker[x] -= 1
    return all(x == 0 for x in tracker.values())

# method 3
from collections import Counter
def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)