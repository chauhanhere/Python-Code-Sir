'''
def reverseword(str):
    spli=str.split(" ")
    wr=[x[::-1]for x in spli]
    print(wr)#it returns a list
    res=''.join(wr)
    print(res)
    return res
str=input("Enter the string")
print(reverseword(str))
'''

def truncateSentence(s, k,v):
    print(' '.join(s.split()[k:-2]))
    print(' '.join(s.split()[:v]))
print(truncateSentence("hghd chdcbdhg dhbcdjdci dcund",-5,3))
