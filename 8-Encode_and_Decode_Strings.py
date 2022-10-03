# 271. Encode and Decode Strings

"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        enstr=""
        for s in strs:
            enstr += (str(len(s))+"#"+s)
        return enstr

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res=[]
        i=0
        while i < len(str):
            j=i
            while str[j] != "#":
                j+=1
            length=int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = (j+1+length)
        return res