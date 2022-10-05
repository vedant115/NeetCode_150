# 125. Valid Palindrome

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# method 1
def isPalindrome(s):
    l, r = 0, len(s)-1
        
    while l < r:
        while l < r and not s[l].isalnum():
            l+=1
        while r > l and not s[r].isalnum():
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True

# method 2 (without using inbuilt functions)
def isPalindrome(s):
    l, r = 0, len(s)-1
        
    while l < r:
        # to check alphanumeric character
        while l < r and not isAlphaNum(s[l]):
            l+=1
        while r > l and not isAlphaNum(s[r]):
            r-=1
            
        # to convert uppercase to lowercase
        cl=s[l]
        cr=s[r]
        if (ord("A") <= ord(cl) <= ord("Z")):
            cl = chr(ord(cl)+32)
        if (ord("A") <= ord(cr) <= ord("Z")):
            cr = chr(ord(cr)+32)
            
        if cl != cr:
            return False
        l, r = l+1, r-1
    return True
    
def isAlphaNum(c):
    return ((ord("A") <= ord(c) <= ord("Z")) or
            (ord("a") <= ord(c) <= ord("z")) or
            (ord("0") <= ord(c) <= ord("9")))