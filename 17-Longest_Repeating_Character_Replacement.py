# 424. Longest Repeating Character Replacement

"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""

# method 1
def characterReplacement(s, k):
		visited = {}
		res = 0
		l = 0
		freq = 0
		for r in range(len(s)):
			visited[s[r]] = 1 + visited.get(s[r], 0)
			freq = max(freq, visited[s[r]])

			while (r - l + 1) - freq> k:
				visited[s[l]] -= 1
				l += 1
			res = max(res, r - l + 1)
		return res

# method 2
def characterReplacement(s, k):
        ans = 0
        i, j = 0, 0
        m = {}
        most_freq = 0
        while j < len(s):
            m[s[j]] = m.get(s[j], 0) + 1
            most_freq = max(most_freq, m[s[j]])
            
            if (j-i+1) - most_freq <= k:
                ans = max(ans, (j-i+1))
                j+=1
            else:
                while (j-i+1) - most_freq > k:
                    m[s[i]] -= 1
                    i += 1
                j+=1
        return ans