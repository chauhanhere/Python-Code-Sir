import collections
def firstUniqChar(s: str):
    c=collections.Counter(list(s))
    for i in range(len(s)):
        if c.get(s[i])==1:
            return i
    return -1
print('index of first unicharacter in the string=',firstUniqChar('loveleetcode'))
