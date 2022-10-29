# 76. Minimum Window Substring

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

def minWindow(s, t):
        i, j = 0, 0
        m = {}
        ans=99999
        res = ""
        for ch in t:
            m[ch] = m.get(ch, 0) + 1
        count = len(m)
        while j < len(s):
            if s[j] in m:
                m[s[j]] -= 1
                if m[s[j]] == 0:
                    count -= 1
            if count > 0:
                j+=1
            elif count == 0:
                while count == 0 and i <= j:
                    if s[i] not in m: 
                        i+=1
                    else:
                        if (ans > j-i+1):
                            ans = j-i+1
                            res = s[i:j+1]
                            
                        m[s[i]] += 1
                        if m[s[i]] > 0:
                            count += 1
                        i+=1 
                j+=1
        return res