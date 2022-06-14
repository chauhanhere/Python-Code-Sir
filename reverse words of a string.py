def reverseword(str):
    words=str.split(" ")
    l=' '.join(reversed(words))
    return l
s=input("Enter a string")
print(reverseword(s))
