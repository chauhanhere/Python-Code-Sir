'''
def twoSum(nums,t):
    d=dict()
    for i in range(len(nums)):
        m=t-nums[i]
        if m in d:
            return [d[m],i]
        else:
            d[nums[i]]=i
s=twoSum([2,11,5,7],9)
print(s)

import collections
def first(n):
    c=collections.Counter(list(n))
    for i in range(len(n)):
        if c.get(n[i])==1:
            return n[i],i
    return -1
print(first("jdnfdj"))

def remove(n):
    l=len(n)
    print(l)
    s=0
    mid=l//2
    for i in range(l):
        print(i)
        s+=n[i][i]
        s+=n[l-1-i][i]
    if l%2==1:
        s-=n[mid][mid]
    return s
print(remove([[1,2,3],[4,5,6],[7,8,9]]))



i=int(input("Enter the amount you have"))
if i>200:
    print("I will give you",i)
else:
    print("I dont have momey to give you")

def singleNumber( nums: list[int]) -> int:
    res=0
    for i in range(0,len(nums)):
        res= res^nums[i]
        print(res)
    return res
print(singleNumber([1,2,1,2,4]))
   
    
a=int(input())
if a==0:
    print("500600")
if a<0:
    print("400")
if a%2!=0:
    print("400")
elif a%2==0 and a>0:
    print("500")

a=int(input())
if a==0:
    print("500600")
if a%2!=0:
    print("400")
elif a%2==0 and a>0:
    print("500")
 
a=int(input("Enter"))
b=int(input("Enter"))
s=a%10
d=b%10
print(s,d)
print(s+d)

input1=int(input('Enter'))
input2=int(input('Enter'))
sum=0
if((input1<10 and input1>0) and (input2<10 and input2>0)):
    sum=input1+input2
    print(sum)
elif(input1<0 and input2<0):
    input1=0-input1
    input2=0-input2
    input1=input1%10
    input2=input2%10
    sum=input1+input2
    print(sum)
elif(input1<0 or input2<0):
    a=input1%10
    b=input2%10
    sum=a-b
    print(sum%10)
else:
    while((input1 >10)or(input2 >10)):
        input1=input1%10
        input2=input2%10
        sum=input1+input2
        print(sum)

s='Suraj'
print(s.isal

def shortestToChar(s, c) -> list[int]:
    n,pos=len(s),-float('inf')
    res=[n]*n
    for i in range(n) + range(n)[::-1]:
        if s[i]==c:
            pos=i
        res[i]=min(res[i],abs(i-pos))
    return res
print(shortestToChar("loveleetcode","e"))
   
       def shortestToChar(self, S, C):
        n, pos = len(S), -float('inf')
        res = [n] * n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res

        def shortestToChar(self, S, C):
           
def findTheDifference(s, t):
    diff = 0
    for i in range(len(s)):
        print(diff)
        diff -= ord(s[i])
        print(diff)
        diff += ord(t[i])
        print(diff)
    diff += ord(t[-1])
    return chr(diff)
print(findTheDifference('abfd','afebd'))

s="mfjkgnt"
v=""
for i in s:
    if i in "abcdefghijklmnopqrstuvwxyz":
        print(i)
        v+=i+" "
print(v)

from collections import Counter
s1 = "this apple is a very sweet apple"
c=Counter(s1.split())
for i in c.elements():
    print(i,c[i])


def findFinalValue(nums,original):
    nums=sorted(nums)
    for i in nums:
        if i==original:
            original=original*2
    return original
print(findFinalValue([5,3,6,1,12],2))

 def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        else:
            evensorted = []
            oddsorted = []
            for i in range(len(nums)):
                if i%2 == 0:
                    evensorted.append(nums[i])
                else:
                    oddsorted.append(nums[i])
            evensorted.sort()
            oddsorted.sort(reverse=True)
            
            evenindex = 0
            oddindex = 0
            for i in range(len(nums)):
                if i%2==0:
                    nums[i] = evensorted[evenindex]
                    evenindex += 1
                else:
                    nums[i] = oddsorted[oddindex]
                    oddindex += 1
        return nums

import socket
'''
#TCP=Reliable,connection oriented protocol socket.SOCK_STREAM
#UDP=connection less protocol socket.SOCK_DGRAM

#IPv4
#Ipv6
'''
con=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST="localhost" #127.0.0.1
PORT=11111 #0-65535 0-1024
con.bind((HOST,PORT))
con.listen()
print("Server is listening")
cl_con,adr=con.accept() #it return two object
print(f"return (adr)")
while True:
    data=input("SERVER:")
    cl_con.send(bytes(data,'utf-8'))#to encrypt the data.Convert to bytes
    cl_data=cl_con.recv(1024).decode()
    print("CLIENT :",CL_data)

cl_con.close()
'''
d=32
s=[1,2,3,89,90,32]
if d in s:
    print(s.index(d))
else:
    print(-1)

















