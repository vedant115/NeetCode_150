# 49. Group Anagrams
"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.
"""

# method 1
import  collections
def groupAnagrams(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

# method 2
def groupAnagrams(strs):
    d = {}
    for s in strs:
        temp = "".join(sorted(s))
        if temp in d:
            d[temp].append(s)
        else:
            d[temp] = [s]
    return (d.values())