# 3. Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):
    ans = 0
    i, j = 0, 0
    m = {}
    while j < len(s):
        m[s[j]] = m.get(s[j], 0) + 1
        
        if len(m) < j-i+1:
            while len(m) < j-i+1:
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    del m[s[i]]
                i+=1
            j+=1
        elif len(m) == j-i+1:
            ans = max(ans, j-i+1)
            j+=1
    return ans