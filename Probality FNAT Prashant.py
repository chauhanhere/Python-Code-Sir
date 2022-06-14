#Probability
#Sum of values greater than the given x,then sum is divided by length of array

count=0
arr="10 8 3 1"

s=arr.split(" ")
#print(len(arr))
l=[]
x=3
for i in list(s):
    l.append(i)
    if int(i)>x:
        count+=1
print(count/len(l))
