# 567. Permutation in String

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

def checkInclusion(s1, s2):
    i, j = 0, 0
    m = {}
    for ch in s1:
        m[ch] = m.get(ch, 0) + 1
    temp = {}
    while j < len(s2):
        temp[s2[j]] = temp.get(s2[j], 0) + 1
        
        if j-i+1 < len(s1):
            j+=1
        elif j-i+1 == len(s1):
            if temp == m:
                return True
            temp[s2[i]] -= 1
            if temp[s2[i]] == 0:
                del temp[s2[i]]
            i+=1
            j+=1
    return False