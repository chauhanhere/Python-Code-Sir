'''
n=int(input("Enter the number to find factorial"))
if n==0:
    print("1")
else:
    f=1
    while(n>=1):
        f=f*(n)
        n=n-1
        if(n==1):
            print("The factorial=",f)
       
import random 
print(random.random())


for i in [1::]:
    print(i)

def decodeString(s):
    stack = []; curNum = 0; curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num*curString
        elif c.isdigit():
            curNum = curNum*10 + int(c)
        else:
            curString += c
    return curString
print(decodeString("3[a]2[bc]"))
'''
def demo(name):
    left,right=0,0
    for c in name:
        if c=='(':
            left,right=left+1,right+1
        elif c==")":
            left,right=left-1,right-1
        else:
            left,right=left-1,right+1
        if right<0:
            return False
        if left<0:
            left=0
    return left==0
print(demo("(*)
           )"))
        


























