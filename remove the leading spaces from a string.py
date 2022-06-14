
def removespace(str):
    words=str.split(" ")
    l=''.join(words)
    return l
s=input("Enter a string")
print(removespace(s))

#OR
'''
n=input("Enter the string")
s=n.replace(' ','')
print(s)
'''
